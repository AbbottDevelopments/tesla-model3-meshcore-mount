"""Orient a Fusion STL export (installed frame) for printing and report bed contact.
mode 'side'  : clip on its +X end face (rotate about Y so +X -> down)
mode 'upright': pocket as installed (floor on the bed)"""
import sys, numpy as np, trimesh
src, dst, mode = sys.argv[1], sys.argv[2], sys.argv[3]
m = trimesh.load(src)
if m.extents.max() < 20: m.apply_scale(10)
if mode == 'side_negx':
    m.apply_transform(trimesh.transformations.rotation_matrix(-np.pi / 2, [0, 1, 0]))  # x' = -z, z' = x  (-X face down)
elif mode == 'side':
    m.apply_transform(trimesh.transformations.rotation_matrix(np.pi / 2, [0, 1, 0]))   # x' = z, z' = -x
m.apply_translation(-m.bounds[0])
m.export(dst)
fz = m.triangles[:, :, 2]; bed = np.all(fz < 1e-3, axis=1)
print(f"{dst.split('/')[-1]}: watertight {m.is_watertight}, size {np.round(m.extents, 2)} mm, vol {m.volume/1000:.2f} cm3, bed contact {m.area_faces[bed].sum():.0f} mm2")
