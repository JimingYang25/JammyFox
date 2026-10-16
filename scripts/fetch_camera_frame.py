"""Fetch a fresh JPEG from the onboard MPU using a direct LAN connection."""
import argparse
import json
import time
import urllib.request
from pathlib import Path
from urllib.parse import urlsplit

MAX_FRAME_BYTES = 5 * 1024 * 1024


def fetch_frame(url, timeout=2, max_frame_age_ms=500):
    if urlsplit(url).scheme not in ('http', 'https'):
        raise ValueError('Expected an HTTP or HTTPS camera URL.')
    # Robot LAN traffic must use the local network regardless of shell proxy settings.
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    start = time.monotonic()
    with opener.open(url, timeout=timeout) as response:
        if response.headers.get_content_type() != 'image/jpeg':
            raise ValueError('Server did not return JPEG data.')
        jpeg = response.read(MAX_FRAME_BYTES + 1)
        age = float(response.headers['X-Frame-Age-Ms'])
        request_duration = (time.monotonic() - start) * 1000
        if not 0 <= age or age + request_duration > max_frame_age_ms:
            raise ValueError('Frame exceeded the cache-age plus request-duration limit.')
        if len(jpeg) > MAX_FRAME_BYTES or not (jpeg.startswith(b'\xff\xd8') and jpeg.endswith(b'\xff\xd9')):
            raise ValueError('Invalid or oversized JPEG response.')
        metadata = {'sequence': int(response.headers['X-Frame-Sequence']),
                    'received_time_ns': int(response.headers['X-Frame-Received-Time-Ns']),
                    'server_cache_age_ms': age,
                    'source': response.headers['X-Frame-Source'],
                    'timestamp_stage': response.headers['X-Timestamp-Stage'],
                    'request_duration_ms': request_duration,
                    'cache_age_plus_request_ms': age + request_duration,
                    'bytes': len(jpeg)}
    return jpeg, metadata


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('url', help='For example: http://MPU_IP:8081/frame.jpg')
    parser.add_argument('--output', type=Path, default=Path('reports/camera/received.jpg'))
    parser.add_argument('--timeout', type=float, default=2)
    args = parser.parse_args()
    jpeg, metadata = fetch_frame(args.url, timeout=args.timeout)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(jpeg)
    args.output.with_suffix('.json').write_text(json.dumps(metadata, indent=2) + '\n')
    print(json.dumps({'saved': str(args.output), **metadata}))


if __name__ == '__main__':
    main()
