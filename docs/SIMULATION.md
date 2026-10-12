# JammyFox MuJoCo assets

[jammyfox.xml](../mjcf/jammyfox.xml) is the floating-base robot; [jammyfox_grasp.xml](../mjcf/jammyfox_grasp.xml) is the fixed-base mouth-grasp contact fixture. Keep the [OBJ assets](../mjcf/assets/) beside the XML files. All mesh filenames and paths are relative, with exact casing for Linux.

These exports were loaded with MuJoCo 3.15.0. The main model has 16 position actuators, 23 position coordinates and 22 velocity coordinates. It includes explicit masses/inertias, joint limits, collision proxies, foot pads and mouth contact surfaces. Units are metres, kilograms, seconds and radians for runtime hinge targets.

Initialize the `standing` keyframe before stepping; it sets both the pose and neutral actuator targets. See the [model usage example](../mjcf/README.md). The model retains the existing CAD mounting limitations. Hardware masses, inertias, servo gains, friction, network timing and actual servo behaviour require calibration.

[model_metadata.json](../mjcf/model_metadata.json) records transforms, mass estimates and original CAD fingerprints. Those fingerprints describe the engineering workspace used to make the export; this repository contains selected exports rather than the complete CAD sources. [robot.json](../config/robot.json) records servo/controller assumptions; [servo_calibration.example.json](../config/servo_calibration.example.json) is an uncalibrated example.

This repository provides the model assets as a starting point for coding. Training environments, policies, inference programs and hardware firmware are not included in this asset copy.
