# JammyFox MJCF — Revision A

`jammyfox.xml` is the floating-base robot model. Keep the adjacent `assets` folder with it; all mesh paths are relative. It contains 16 position actuators, joint limits, explicit masses/inertias, collision proxies, four foot pads and mouth contact surfaces. Units are metres, kilograms and seconds; control targets are hinge angles in radians.

**Initialize the `standing` keyframe before stepping.** It includes both the standing joint pose and neutral actuator targets.

```python
import mujoco

model = mujoco.MjModel.from_xml_path("jammyfox.xml")
data = mujoco.MjData(model)
mujoco.mj_resetDataKeyframe(model, data, model.key("standing").id)
mujoco.mj_forward(model, data)

for _ in range(500):
    mujoco.mj_step(model, data)
```

Actuator names are `<joint_name>_servo`; for example, set `data.ctrl[model.actuator("neck_yaw_servo").id]` to a target in radians within its control range.

`jammyfox_grasp.xml` is a separate contact-test fixture with a fixed robot base and a free test object. The main `jammyfox.xml` retains its floating base. Neither model welds objects to the mouth.

The files were loaded and checked with MuJoCo 3.15.0. The robot has 23 position coordinates, 22 velocity coordinates and 16 actuators. `model_metadata.json` records CAD transforms, mass estimates and provenance. The nominal mass is 3.177 kg; hardware masses, inertias, servo gains and friction still need calibration. The XML includes position PD and torque caps; network delay and target slew are external-controller concerns. CAD mounting details remain those of the existing review revision.
