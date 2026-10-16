# JammyFox

A Minecraft-style fox robot designed around a 50 cm body, PLA printed parts and 16 FEETECH ST-3215-C018 12 V bus servos. The current goals are walking, mouth grasping, head shaking and tail swinging. The onboard MPU/MCU communicates over Wi-Fi with an external Jetson Orin Nano Super 8 GB; the RTX 5090 workstation is used for simulation, training and testing.

This repository contains the selected fabrication and MuJoCo assets from CAD Revision A, plus a removable USB RGB camera accessory.

## Start here

- [BOM and China purchase links](docs/BOM.md)
- [Screws, nuts and washers](docs/FASTENERS.md)
- [Mechanical notes and validation limits](docs/MECHANICAL.md)
- [Bambu Studio printing guide](printable/README.md)
- [First fit-test plate](printable/plates/00_fit_test.3mf)
- [MuJoCo model notes](docs/SIMULATION.md)
- [Floating-base MJCF](mjcf/jammyfox.xml) and [grasp fixture](mjcf/jammyfox_grasp.xml)

- [USB RGB camera, CAD, purchase links and live view](docs/CAMERA.md)

## Layout

```text
JammyFox/
  docs/        BOM, fasteners, mechanical and simulation notes
  stl/         53 individual printable meshes in millimetres
  printable/   53 individual 3MF files, 15 plates and print guides
  drawings/    Aluminum chassis DXF/SVG and hole coordinates
  mjcf/        Base/camera MJCF models, metadata and 167 OBJ assets
  hardware/    Camera CAD assembly, source and reference geometry
  scripts/     Preview, RGB capture and MPU/Jetson frame transport
  config/      CAD dimensions and servo/controller assumptions
  metadata/    Quantities, joint axes, fasteners and verification reports
```

Production plates and individual part files are alternative ways to print the same robot set. Start with the fit-test plate. Select your actual printer, nozzle and PLA profile in Bambu Studio; these are geometry files without machine toolpaths or generated supports.

## Load the model

From the repository root, in your WSL Conda environment:

```bash
python -m pip install -r requirements.txt
```

```python
import mujoco

model = mujoco.MjModel.from_xml_path('mjcf/jammyfox_camera.xml')
data = mujoco.MjData(model)
mujoco.mj_resetDataKeyframe(model, data, model.key('standing').id)
mujoco.mj_forward(model, data)
```

## Revision status

The CAD is an engineering review revision. Physical fit, strength, walking and grasping have not been validated, and several frame, foot and enclosure attachment details still need completion. Valid meshes and a loadable simulator model do not establish that the whole robot is assembly-ready. See the mechanical notes before printing the full set.

Native CAD sources, local runtimes, historical archives, training runs and duplicate ZIP bundles remain in the original engineering workspace. `file_manifest.json` records SHA-256 hashes for the selected repository files. Existing CAD fingerprints in export metadata retain their original provenance.
