"""Editor declarations for the MuJoCo 3.15.0 APIs used by JammyFox."""

from typing import ClassVar, SupportsIndex, SupportsInt

import mujoco._structs as _structs
from mujoco._structs import *
from mujoco.rendering.classic.renderer import Renderer as Renderer

def mj_step(
    m: _structs.MjModel, d: _structs.MjData, nstep: SupportsInt | SupportsIndex = 1
) -> None: ...
def mj_forward(m: _structs.MjModel, d: _structs.MjData) -> None: ...
def mj_resetDataKeyframe(
    m: _structs.MjModel, d: _structs.MjData, key: SupportsInt | SupportsIndex
) -> None: ...

class mjtCamera:
    mjCAMERA_FREE: ClassVar[mjtCamera]
    mjCAMERA_TRACKING: ClassVar[mjtCamera]
    mjCAMERA_FIXED: ClassVar[mjtCamera]
    mjCAMERA_USER: ClassVar[mjtCamera]

    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __index__(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...
