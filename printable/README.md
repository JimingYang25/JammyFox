# JammyFox Rev A printable 3MF

Target slicer: Bambu Studio. These are standard 3MF **model files** containing
millimetre geometry, part names, instances and arranged positions. Select your
actual printer/nozzle/bed and PLA profile in Bambu Studio before slicing. Import
geometry if prompted; printer settings, support structures and toolpaths are not
embedded. The files are not a Bambu machine-specific project or sliced job.

## Files

- `plates/00_fit_test.3mf`: one clamp pair, a horn coupon, five nominal interface
  spacers and five alternate spacer thicknesses; 13 test pieces.
- `plates/01_...` onward: 13 production plates containing
  exactly 117 physical pieces for the current CAD BOM.
- `parts/`: 51 files, one per printable CAD part type, including
  optional fit pieces. Each standoff-kit file contains four separate posts.
- `plate_inventory.csv`: placement quantities, orientations and support notes.
- `plate_overview.png` and `previews/`: top-view plate guides.
- `verification.json`: conversion/quantity/placement checks and source hashes.

Production plates and individual files are alternative ways to print the same
parts; printing both duplicates the robot set. The fit-test plate is extra and
does not reduce the production quantities. Bought servos, metal horns, boards,
battery and the two aluminum chassis plates are excluded from the print files.

## Bed and placement

The printer model was not specified. Layouts assume a 220 x 220 x
220 mm volume, 10 mm edge margins and at least 8 mm between
object bounding boxes. Each object is placed at Z=0. Confirm the actual usable
bed area, exclusion zones and brim/support footprint after importing. Print by
layer rather than using a sequential object-printing mode with these layouts.
Display colors are only a guide; assign the intended single PLA spool for each
plate. The hidden horn spacers are grouped with black hardware.

## Slicing starting points

Use your calibrated printer profile. For a 0.4 mm nozzle, 0.2 mm layers are a
starting point. The 0.6 mm spacer is only three nominal layers thick, so inspect
its sliced thickness. Use 100% infill for spacers and the fit coupon; start with
5-6 walls and 35-45% infill for clamps, feet, forks and mounts. Hollow shells can
start with 4 walls and 10-15% infill. These are trial settings, not validated
strength or temperature specifications for your printer/filament.

Body roofs, trays, the muzzle and hollow tail pieces were oriented to open their
cavities upward or place a broad face on the bed. Forks use side/end orientations
to reduce large suspended plates. Check horizontal bores and horn-disc edges.
Enable and inspect supports for pedestal upper plates, roll-fork bridges and
raised head-lid ledges. Where support must begin on the model, use an everywhere
support setting and check removal access. A 5 mm brim is a starting point for
tall posts, the tail shell and upright forks. Support and brim footprints can
extend beyond the model rectangles and must be reviewed in the sliced preview.

## Fit and CAD status

Start with the fit-test plate and an actual C018 servo/horn set. Check clearances,
spacer thicknesses and screw engagement before printing the full set. The export
preserves Rev A geometry: remaining frame/case anchors, foot-ear mating details,
cover nut seats and shell attachments still need completion. A watertight,
sliceable mesh does not establish that the entire robot is assembly-ready.

The files were checked against the core 3MF XML schema, reloaded using trimesh,
and checked for watertight surfaces, unchanged volumes/placements, counts,
Z=0 placement, model-bed bounds and rectangle spacing. Bambu Studio was not
installed in the locations inspected on this workstation; a Bambu UI import or
machine-specific slicing test has not been performed.

Format references: [3MF Consortium core specification](https://github.com/3MFConsortium/spec_core/blob/master/3MF%20Core%20Specification.md)
and [Bambu Studio 3MF/CLI documentation](https://github.com/bambulab/BambuStudio/wiki/Command-Line-Usage).

The source meshes are in [stl](../stl/) and the part quantities are in
[part_inventory.json](../metadata/part_inventory.json). CAD and 3MF generation
tools remain in the original engineering workspace. Update fabrication and
simulation exports together after geometry changes.
