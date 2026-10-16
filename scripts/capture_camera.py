"""Save a head-mounted camera RGB frame without an OpenCV dependency."""
import argparse
import json
import math
import struct
import zlib
from pathlib import Path

import mujoco


def write_png(path, image):
    height, width, channels = image.shape
    if channels != 3 or str(image.dtype) != 'uint8':
        raise ValueError('Expected a uint8 RGB image.')

    def chunk(kind, data):
        return (struct.pack('!I', len(data)) + kind + data
                + struct.pack('!I', zlib.crc32(kind + data) & 0xffffffff))

    scanlines = b''.join(b'\0' + row.tobytes() for row in image)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(
        b'\x89PNG\r\n\x1a\n'
        + chunk(b'IHDR', struct.pack('!2I5B', width, height, 8, 2, 0, 0, 0))
        + chunk(b'IDAT', zlib.compress(scanlines, 6))
        + chunk(b'IEND', b'')
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--demo', action='store_true')
    parser.add_argument('--yaw-deg', type=float, default=0)
    parser.add_argument('--pitch-deg', type=float, default=0)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    config = json.loads((root / 'config/camera.json').read_text())
    filename = 'jammyfox_camera_demo.xml' if args.demo else 'jammyfox_camera.xml'
    model = mujoco.MjModel.from_xml_path(str(root / 'mjcf' / filename))
    data = mujoco.MjData(model)
    mujoco.mj_resetDataKeyframe(model, data, model.key('standing').id)
    for name, degrees in [('neck_yaw', args.yaw_deg), ('neck_pitch', args.pitch_deg)]:
        angle = math.radians(degrees)
        lo, hi = model.joint(name).range
        if not lo <= angle <= hi:
            parser.error(f'{name} angle is outside the model joint limits.')
        data.joint(name).qpos[:] = angle
    mujoco.mj_forward(model, data)
    width, height = config['capture_resolution']
    with mujoco.Renderer(model, height=height, width=width) as renderer:
        renderer.update_scene(data, camera='head_rgb')
        rgb = renderer.render().copy()
    path = args.output or root / 'reports/camera/head_rgb.png'
    write_png(path, rgb)
    print(f'Saved {width}x{height} RGB camera frame: {path}')


if __name__ == '__main__':
    main()
