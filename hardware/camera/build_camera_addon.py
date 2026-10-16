"""Build a removable USB camera accessory using the existing head-lid holes."""
import hashlib
import json
import math
from pathlib import Path

import FreeCAD as App
import Import
import Mesh
import Part

SCRIPT = Path(__file__).resolve()
PORTABLE = SCRIPT.parent.name == 'camera'
CAD = SCRIPT.parents[1]
OUT = SCRIPT.parent / 'generated' if PORTABLE else CAD / 'output/camera'
OUT.mkdir(exist_ok=True)
config_path = SCRIPT.parent / 'camera_addon.json' if PORTABLE else CAD / 'config/camera_addon.json'
P = json.loads(config_path.read_text())
V = App.Vector


def box(x, y, z, dx, dy, dz):
    return Part.makeBox(dx, dy, dz, V(x, y, z))


def cylinder_x(radius, length, x, y, z):
    return Part.makeCylinder(radius, length, V(x, y, z), V(1, 0, 0))


def fuse(shapes):
    result = shapes[0]
    for shape in shapes[1:]:
        result = result.fuse(shape)
    return result.removeSplitter()


def hex_pocket_x(x, y, z, across_flats=4.3, depth=1.8):
    radius = across_flats / math.sqrt(3)
    points = [V(x, y + radius * math.cos(a), z + radius * math.sin(a))
              for a in [i * math.pi / 3 for i in range(6)]]
    return Part.Face(Part.makePolygon(points + [points[0]])).extrude(V(depth, 0, 0))


bridge = fuse([
    box(278, -49, 325, 8, 98, 3),
    box(278, -15.5, 325, 19, 31, 3),
    box(294, -15.5, 325, 3, 31, 12),
])
for x, y, _ in P['head_lid_front_holes_cad_mm']:
    bridge = bridge.cut(Part.makeCylinder(1.7, 5, V(x, y, 324)))
for y in (-10.5, 10.5):
    bridge = bridge.cut(cylinder_x(1.7, 5, 293, y, 332))
for y in (-10, 10):
    bridge = bridge.cut(box(287, y - 1, 324, 6, 2, 5))
bridge = bridge.removeSplitter()

carrier = box(297, -15.5, 289.5, 3, 31, 47.5)
carrier = carrier.cut(box(296, -8.5, 296.5, 5, 17, 17))
# Clearance for the camera's lower-edge USB connector and cable.
carrier = carrier.cut(box(296, -7, 289, 10, 14, 9))
for y in (-10.5, 10.5):
    for z in (294.5, 315.5):
        carrier = carrier.fuse(cylinder_x(3, 5, 300, y, z))
        carrier = carrier.cut(cylinder_x(1.2, 11, 296, y, z))
        carrier = carrier.cut(hex_pocket_x(297, y, z))
for y in (-10.5, 10.5):
    carrier = carrier.cut(cylinder_x(1.7, 5, 296, y, 332))
carrier = carrier.removeSplitter()

board = box(305, -12.5, 292.5, 1.6, 25, 25)
for y in (-10.5, 10.5):
    for z in (294.5, 315.5):
        board = board.cut(cylinder_x(1.0, 4, 304, y, z))
module = fuse([
    board,
    box(300.5, -8, 297, 4.5, 16, 16),
    box(306.6, -8, 297, 6, 16, 16),
    cylinder_x(7, 16, 306.6, 0, 305),
])

parts = {
    'camera_lid_bridge': (bridge, 'PLA', [0.1, 0.105, 0.12]),
    'camera_board_carrier': (carrier, 'PLA', [0.1, 0.105, 0.12]),
    'usb_rgb_camera_module': (module, 'Purchased', [0.08, 0.2, 0.12]),
}
for name, (shape, material, _) in parts.items():
    if not shape.isValid() or len(shape.Solids) != 1:
        raise RuntimeError('Invalid or disconnected accessory: ' + name)
for a, b in [('camera_lid_bridge', 'camera_board_carrier'),
             ('camera_lid_bridge', 'usb_rgb_camera_module'),
             ('camera_board_carrier', 'usb_rgb_camera_module')]:
    overlap = parts[a][0].common(parts[b][0]).Volume
    if overlap > 0.001:
        raise RuntimeError('Accessory parts overlap: ' + a + ' / ' + b)

source = SCRIPT.parent / 'RevA_reference.FCStd' if PORTABLE else CAD / 'output/JammyFox_RevA.FCStd'
source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
original = App.openDocument(str(source))
references = [obj for obj in original.Objects if hasattr(obj, 'Shape') and hasattr(obj, 'RigidGroup')]
if len(references) != 164:
    raise RuntimeError('Unexpected original assembly size')
for name, (shape, _, _) in parts.items():
    for obj in references:
        if shape.BoundBox.intersect(obj.Shape.BoundBox) and shape.common(obj.Shape).Volume > 0.001:
            raise RuntimeError('Accessory intersects existing CAD: ' + name + ' / ' + obj.Name)

sampled = []
for yaw in (-20, 0, 20):
    yaw_pose = App.Placement(V(188, 0, 247), App.Rotation(V(0, 0, 1), yaw)).multiply(
        App.Placement(V(-188, 0, -247), App.Rotation()))
    for pitch in (-15, 0, 15):
        pitch_pose = App.Placement(V(228, 0, 285), App.Rotation(V(0, 1, 0), pitch)).multiply(
            App.Placement(V(-228, 0, -285), App.Rotation()))
        pose = yaw_pose.multiply(pitch_pose)
        for name, (shape, _, _) in parts.items():
            moving = shape.copy()
            moving.Placement = pose.multiply(moving.Placement)
            for obj in references:
                if obj.RigidGroup in ('neck_pitch', 'jaw'):
                    continue
                reference = obj.Shape.copy()
                if obj.RigidGroup == 'neck_yaw':
                    reference.Placement = yaw_pose.multiply(reference.Placement)
                if moving.BoundBox.intersect(reference.BoundBox) and moving.common(reference).Volume > 0.001:
                    raise RuntimeError('Neck-limit intersection: ' + name + ' / ' + obj.Name)
        sampled.append({'yaw_deg': yaw, 'pitch_deg': pitch})

doc = App.newDocument('JammyFox_USB_RGB_Camera')
objects = []
for old in references:
    new = doc.addObject('Part::Feature', old.Name)
    new.Label = old.Label
    new.Shape = old.Shape.copy()
    for prop in ('PartNumber', 'RigidGroup', 'Material'):
        new.addProperty('App::PropertyString', prop)
        setattr(new, prop, getattr(old, prop))
    objects.append(new)

records = []
addon_objects = []
for name, (shape, material, color) in parts.items():
    obj = doc.addObject('Part::Feature', name)
    obj.Shape = shape
    obj.addProperty('App::PropertyString', 'RigidGroup').RigidGroup = 'neck_pitch'
    obj.addProperty('App::PropertyString', 'Material').Material = material
    obj.addProperty('App::PropertyString', 'PartNumber').PartNumber = name
    if App.GuiUp:
        obj.ViewObject.ShapeColor = tuple(color)
    addon_objects.append(obj)
    Import.export([obj], str(OUT / (name + '.step')))
    vertices, faces = shape.tessellate(0.2)
    mass_g = shape.Volume * P['pla_density_g_mm3'] if material == 'PLA' else P['module_mass_estimate_g']
    record = {'name': name, 'material': material, 'mass_g': mass_g,
              'mass_measured': False, 'volume_mm3': shape.Volume,
              'vertices_cad_mm': [[v.x, v.y, v.z] for v in vertices],
              'faces': [list(face) for face in faces], 'color': color}
    if material == 'PLA':
        print_shape = shape.copy()
        if name == 'camera_board_carrier':
            print_shape.rotate(V(0, 0, 0), V(0, 1, 0), -90)
        bounds = print_shape.BoundBox
        print_shape.translate(V(-(bounds.XMin + bounds.XMax) / 2,
                                -(bounds.YMin + bounds.YMax) / 2, -bounds.ZMin))
        verts, triangles = print_shape.tessellate(0.2)
        Mesh.Mesh([[verts[i] for i in face] for face in triangles]).write(str(OUT / (name + '.stl')))
        record['print_bounds_mm'] = [print_shape.BoundBox.XLength, print_shape.BoundBox.YLength, print_shape.BoundBox.ZLength]
    records.append(record)

doc.recompute()
doc.saveAs(str(OUT / 'JammyFox_USB_RGB_Camera.FCStd'))
Import.export(objects + addon_objects, str(OUT / 'JammyFox_USB_RGB_Camera.step'))
Import.export(addon_objects, str(OUT / 'USB_Camera_Addon.step'))
report = {'revision': P['revision'], 'source_fcstd_sha256': source_hash,
          'original_components': 164, 'new_components': 3, 'parts': records,
          'neck_poses_checked': sampled, 'sampled_intersections': 0,
          'nominal_static_intersections': 0,
          'pcb_holes_mm': [[305, y, z] for y in (-10.5, 10.5) for z in (294.5, 315.5)],
          'nominal_optical_reference_cad_mm': [322.6, 0, 305],
          'added_mass_estimate_g': sum(record['mass_g'] for record in records),
          'fasteners_and_cables_in_mass': False, 'physical_fit_verified': False,
          'component_envelopes': 'PCB, hole pattern, overall depth and lens diameter are manufacturer dimensions; rear electronics and lens-holder shapes are conservative approximations.'}
(OUT / 'camera_cad.json').write_text(json.dumps(report, indent=2))
App.closeDocument(doc.Name)
App.closeDocument(original.Name)
if hashlib.sha256(source.read_bytes()).hexdigest() != source_hash:
    raise RuntimeError('Original CAD was modified')
print('CAMERA_CAD_BUILT', len(records), 'parts; added mass g:', report['added_mass_estimate_g'])
