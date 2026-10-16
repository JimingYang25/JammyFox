import math
import time
from pathlib import Path

import mujoco
import mujoco.viewer

root = Path(__file__).resolve().parents[1]
model = mujoco.MjModel.from_xml_path(str(root / "mjcf/jammyfox_camera_demo.xml"))

