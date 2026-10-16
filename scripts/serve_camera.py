"""Serve the latest USB MJPEG frame over LAN; optionally replay a test JPEG."""
import argparse
import json
import shutil
import subprocess
import threading
import time
from dataclasses import dataclass
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

MAX_FRAME_BYTES = 5 * 1024 * 1024


@dataclass(frozen=True)
class Frame:
    jpeg: bytes
    sequence: int
    received_time_ns: int
    received_monotonic: float
    source: str


class LatestFrame:
    def __init__(self):
        self.lock = threading.Lock()
        self.frame = None
        self.sequence = 0
        self.error = None

    def publish(self, jpeg, source):
        if not (0 < len(jpeg) <= MAX_FRAME_BYTES and jpeg.startswith(b'\xff\xd8') and jpeg.endswith(b'\xff\xd9')):
            raise ValueError('Invalid or oversized JPEG frame')
        with self.lock:
            self.sequence += 1
            self.frame = Frame(jpeg, self.sequence, time.time_ns(), time.monotonic(), source)
            self.error = None

    def snapshot(self, max_age):
        with self.lock:
            frame = self.frame
        if frame is None or time.monotonic() - frame.received_monotonic > max_age:
            return None
        return frame

    def fail(self, error):
        with self.lock:
            self.error = str(error)


def read_multipart_jpegs(stream):
    """Read FFmpeg's mpjpeg output by Content-Length, not JPEG marker scanning."""
    while True:
        length = None
        for _ in range(64):
            line = stream.readline(4097)
            if not line:
                return
            if len(line) > 4096:
                raise ValueError('Oversized multipart header')
            if line.lower().startswith(b'content-length:'):
                length = int(line.split(b':', 1)[1].strip())
            if not line.strip() and length is not None:
                break
        else:
            raise ValueError('Invalid multipart frame headers')
        if length is None or not 0 < length <= MAX_FRAME_BYTES:
            raise ValueError('Invalid multipart frame length')
        jpeg = stream.read(length)
        if len(jpeg) != length:
            raise EOFError('Truncated camera frame')
        yield jpeg


class Capture:
    def __init__(self, args, latest):
        self.args = args
        self.latest = latest
        self.stop_event = threading.Event()
        self.process = None
        self.thread = threading.Thread(target=self.run, daemon=True)

    def run(self):
        try:
            if self.args.test_image:
                jpeg = self.args.test_image.read_bytes()
                while not self.stop_event.is_set():
                    self.latest.publish(jpeg, 'test_image')
                    self.stop_event.wait(1 / self.args.fps)
                return
            width, height = self.args.resolution
            command = [self.args.ffmpeg, '-hide_banner', '-loglevel', 'error', '-nostdin',
                       '-f', 'v4l2', '-input_format', 'mjpeg', '-video_size', f'{width}x{height}',
                       '-framerate', str(self.args.fps), '-i', self.args.device,
                       '-an', '-c:v', 'copy', '-f', 'mpjpeg', 'pipe:1']
            self.process = subprocess.Popen(command, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE)
            for jpeg in read_multipart_jpegs(self.process.stdout):
                if self.stop_event.is_set():
                    break
                self.latest.publish(jpeg, 'usb_capture_pipe')
            if not self.stop_event.is_set():
                self.latest.fail('USB capture stopped; check device, formats, permissions and FFmpeg output.')
        except (OSError, ValueError, EOFError) as error:
            self.latest.fail(error)
        finally:
            self.stop_process()

    def stop_process(self):
        process = self.process
        if process is not None and process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()

    def close(self):
        self.stop_event.set()
        self.stop_process()
        self.thread.join(timeout=4)


def handler_for(latest, max_age):
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.respond(False)

        def do_HEAD(self):
            self.respond(True)

        def respond(self, head_only):
            self.connection.settimeout(2)
            path = urlsplit(self.path).path
            frame = latest.snapshot(max_age)
            if path == '/health':
                payload = json.dumps({'ready': frame is not None,
                                      'sequence': latest.sequence, 'error': latest.error,
                                      'timestamp_stage': 'frame_received_by_server'}).encode()
                self.send_response(200 if frame else 503)
                self.send_header('Content-Type', 'application/json')
            elif path == '/frame.jpg' and frame:
                payload = frame.jpeg
                self.send_response(200)
                self.send_header('Content-Type', 'image/jpeg')
                self.send_header('X-Frame-Sequence', str(frame.sequence))
                self.send_header('X-Frame-Received-Time-Ns', str(frame.received_time_ns))
                self.send_header('X-Frame-Age-Ms', f'{(time.monotonic() - frame.received_monotonic) * 1000:.3f}')
                self.send_header('X-Frame-Source', frame.source)
                self.send_header('X-Timestamp-Stage', 'frame_received_by_server')
            elif path == '/frame.jpg':
                payload = b'No fresh camera frame available.'
                self.send_response(503)
                self.send_header('Content-Type', 'text/plain')
            else:
                self.send_error(404)
                return
            self.send_header('Cache-Control', 'no-store')
            self.send_header('Content-Length', str(len(payload)))
            self.end_headers()
            if head_only:
                return
            try:
                self.wfile.write(payload)
            except (BrokenPipeError, ConnectionResetError, TimeoutError):
                pass

        def log_message(self, format, *args):
            pass

    return Handler


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bind', default='127.0.0.1')
    parser.add_argument('--port', type=int, default=8081)
    parser.add_argument('--device', default='/dev/video0')
    parser.add_argument('--resolution', type=int, nargs=2, default=[1280, 720], metavar=('WIDTH', 'HEIGHT'))
    parser.add_argument('--fps', type=int, default=30)
    parser.add_argument('--max-frame-age', type=float, default=.5)
    parser.add_argument('--test-image', type=Path, help='Replay a JPEG for a transport test; no camera or FFmpeg required.')
    parser.add_argument('--ffmpeg', default='ffmpeg')
    args = parser.parse_args()
    if args.fps <= 0 or args.max_frame_age <= 0 or min(args.resolution) <= 0 or not 0 <= args.port <= 65535:
        parser.error('Invalid rate, resolution, frame-age or port.')
    if not args.test_image and shutil.which(args.ffmpeg) is None:
        parser.error('USB capture requires FFmpeg. Install the system ffmpeg package on the MPU.')
    if args.test_image:
        jpeg = args.test_image.read_bytes()
        if not (jpeg.startswith(b'\xff\xd8') and jpeg.endswith(b'\xff\xd9') and len(jpeg) <= MAX_FRAME_BYTES):
            parser.error('--test-image must be a JPEG, not a PNG.')
    latest = LatestFrame()
    capture = Capture(args, latest)
    with ThreadingHTTPServer((args.bind, args.port), handler_for(latest, args.max_frame_age)) as server:
        capture.thread.start()
        print(f'Camera frames: http://{args.bind}:{server.server_port}/frame.jpg', flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            capture.close()


if __name__ == '__main__':
    main()
