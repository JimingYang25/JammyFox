# JammyFox mechanical notes — Revision A

Exported fabrication assets for the 50 cm fox with 16 FEETECH ST-3215-C018 bus servos. The current functions are walking, mouth grasping, head movement and tail movement.

## Files

- [STL meshes](../stl/): individual printed parts; dimensions are millimetres.
- [Printable 3MF guide](../printable/README.md): individual parts, arranged production plates and the extra fit-test plate.
- [Mechanical BOM](../metadata/mechanical_BOM.csv): material and quantity per part; quantity-zero rows are optional fit pieces.
- [Chassis drawings](../drawings/): DXF, SVG and hole coordinates for two 2 mm aluminum plates, in millimetres.
- [Joint axes](../metadata/joint_axes.csv), [CAD verification](../metadata/verification_summary.json) and [sampled interference report](../metadata/interference_report.json).
- [Fastener specification](FASTENERS.md), [purchasing schedule](../metadata/fasteners.csv), [horn interfaces](../metadata/fastener_interfaces.csv) and [stack arithmetic](../metadata/fastener_summary.json).

The native SolidWorks/FreeCAD files and CAD generation tools remain in the original engineering workspace. The exported geometry here preserves that review revision.

## Hardware interfaces

The selected servo is **FEETECH ST-3215-C018, 12 V / 30 kg·cm**, from the user's [confirmed JD package](https://item.jd.com/10205990758166.html). The selected-servo dimensions are the C018 dimensions confirmed in the engineering workspace.

The case reference is 45.23 x 24.73 x 35 mm. The supplied metal horns use a 14 mm bolt circle with four M3 fasteners. Servo representation is a conservative outer envelope, not a model of gears or spline teeth. The generator uses the C018 horn dimensions rather than the older generic SCS215 download. The provided package brackets have not been dimensionally confirmed; this revision uses replaceable printed case clamps and the supplied metal horns.

Nominal case clearance is 0.35 mm per side. Horn spacers close the gap from the nominal stock disc faces to the moving carriers. Their axial thickness must be confirmed against the actual servo/horns; alternate spacers and a 14 mm bolt-circle coupon are supplied. Use the metal splined horn from the servo package. Do not print a substitute spline.

The ZERO 3W and ESP32 board models are envelope placeholders. The removable tray uses long mounting slots to avoid assuming an exact module hole pattern. The ESP32 reference board uses 58 x 23 mm mounting spacing; use M2.5 board hardware where its holes require it. Confirm module revision, connectors, battery dimensions and cable exits on the real parts.

## Structure and assembly

The chassis has two connected 2 mm aluminum plates, four short printed rails, fixed hip mounts and separate battery crossbars. The shell is split into front/rear sections. Covers use removable standoffs; the head has a raised removable cover for pitch-stage clearance. The battery and electronics occupy separate bays.

Each leg uses a hip roll joint, hip pitch joint and knee. The pitch and knee forks are separated laterally so they can move without their plates overlapping. Both stock horn sides are represented. The feet are rigid PLA, with attachment ears and matching shin bores. The tail is hollow PLA with a white tip and a flange at its root.

Generic case clamp halves use four M3 through bolts. Carrier interfaces use four M3 holes on the stock horn pattern. The fastener supplement selects M3 x 0.5 ISO 4762 / DIN 912 steel socket-head screws, metal washers and M3 locknuts. The 30 connected horn faces require 120 coupling screws. Nominal horn lengths are M3 x 8/10/12/14/18 with a 1.5 mm head-washer stack; these require calibration to actual horn/spacer dimensions. Standalone clamp bolts are nominal M3 x 50; longer shared neck-yaw/tail pedestal bolts are held for detailing. Original servo centre screws remain separate from coupling screws.

This supplement does not modify the CAD geometry or complete its attachment features. Frame-rail/hip anchors, case-to-carrier connections, foot-ear clearance/anti-rotation, cover nut seats, and shell/accessory mounts still need detailing. The geometry check excludes parts in the same rigid group; it does not prove that these static mating interfaces are physically assemblable. The released model is still a review package, not a complete production fastener schedule. Hardware heads, nuts and tips were not included in the original motion checks.

Suggested order: chassis and rails; hip modules; thigh/knee modules; shin/feet; neck and jaw; tail; battery and board trays; wiring; removable covers. Zero each servo at the intended mechanical pose before coupling the metal horns.

## What the checks establish

The checks verify valid solid geometry, connected structural parts, watertight print meshes, fit within an assumed 220 x 220 x 220 mm print volume, and sampled intersections between moving rigid groups. The four-piece cover-standoff kits intentionally contain separate bodies.

Motion checks include standing, individual joint-type range endpoints and combined neck-yaw/pitch/jaw endpoints. They are sampled poses, not proof of every continuous motion or every possible simultaneous leg configuration. The actual results and scope are recorded in the JSON reports.

The geometry-based mass estimate is conservative for fully solid PLA and nominal purchased-part masses. It excludes unmodeled screws, nuts, cables and power hardware. It is above the early 2-2.5 kg target. Weigh the printed assembly and validate motor loads; do not use the estimate as a measured mass. Native part appearances are colors, not calibrated SolidWorks material definitions for FEA.

This is a review CAD package. Printed fit, assembly strength, thermal behavior, grasping and walking performance have not been physically validated. No FEA or functioning controller is included. Start with slow walking on level ground and objects positioned at the mouth, as agreed in the BOM.

## First fit trial

Print one pair of servo clamps, one horn coupon, and the selected interface spacer. Fit them to one actual C018 servo and both supplied horns. Check clearance, screw engagement, connector access and free rotation. Adjust the clearance/spacer dimensions before printing the full set. Also trial the board tray and battery bay with the selected hardware.

For a 0.4 mm nozzle, 0.2 mm layers are a reasonable starting point. Clamp walls, bolt interfaces and narrow carrier borders need multiple perimeters. Use supports where the forks or enclosure overhangs require them. Print meshes are centered in XY and placed on Z=0; print orientation and support strategy remain the operator's choice.

The standard 3MF export supplies suggested orientations and separate, nonoverlapping plate placements at Z=0. It is intended for geometry import into Bambu Studio; select your actual printer, nozzle and filament profile before slicing. Support structures and machine toolpaths are not embedded. Conversion checks preserve STL geometry/volumes, validate core XML, reload all objects with an independent reader, and check quantities and model-bed bounds. These files retain the incomplete attachment details of CAD Revision A.
