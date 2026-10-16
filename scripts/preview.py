"""Inspect JammyFox, its USB camera, and servo movement with GUI sliders."""
import argparse
import time
from pathlib import Path

import mujoco
import mujoco.viewer


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--camera', choices=['free', 'overview', 'mouth_view', 'head_rgb'], default='free')
    parser.add_argument('--demo', action='store_true', help='Add red/blue visual camera targets.')
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    filename = 'jammyfox_camera_demo.xml' if args.demo else 'jammyfox_camera.xml'
    model = mujoco.MjModel.from_xml_path(str(root / 'mjcf' / filename))
    data = mujoco.MjData(model)
    mujoco.mj_resetDataKeyframe(model, data, model.key('standing').id)
    mujoco.mj_forward(model, data)

    frame_period = 1.0 / 50.0
    steps_per_frame = max(1, round(frame_period / model.opt.timestep))
    with mujoco.viewer.launch_passive(model, data) as viewer:
        if args.camera != 'free':
            with viewer.lock():
                viewer.cam.type = mujoco.mjtCamera.mjCAMERA_FIXED
                viewer.cam.fixedcamid = model.camera(args.camera).id
        while viewer.is_running():
            frame_start = time.perf_counter()
            for _ in range(steps_per_frame):
                mujoco.mj_step(model, data)
            # Receives GUI actuator commands as well as displaying physics.
            viewer.sync()
            remaining = frame_period - (time.perf_counter() - frame_start)
            if remaining > 0:
                time.sleep(remaining)


if __name__ == '__main__':
    main()
