import numpy as np
from CameraLookingAt import *
from rasterize import *
from render import *

def RenderObject(p3d, faces, vcolors, H, W, Rows, Columns, f, cv, cK, cup):
    p2d, depth = CameraLookingAt(f, cv, cK, cup, p3d)
    p2d = rasterize(p2d, Rows, Columns, H, W)
    p2d = np.array(p2d).astype(int) # Pixels are integers
    # Numpy arrays to python lists
    p2d = p2d.tolist()
    faces = faces.tolist()
    vcolors = vcolors.tolist()
    depth = depth.tolist()
    I = render(p2d, faces, vcolors, depth, "gouraud")
    return I