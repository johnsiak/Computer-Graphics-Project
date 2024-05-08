import numpy as np
from PinHole import *

def CameraLookingAt(f, cv, cK, cup, p3d):
    # Flattening of the arrays because I want to change the dimensions from (3,1) to (3,)
    cv = cv.flatten()
    cK = cK.flatten()
    cup = cup.flatten()
    cK = np.array(cK) + np.array(cv) # cK
    cz = cK/np.linalg.norm(cK) # Normalise vector
    t = np.array(cup - np.dot(cup, cz)*cz) # Calculate t
    cy = t/np.linalg.norm(t) # Normalise vector
    cx = np.cross(cy, cz) # Cross product
    p2d, depth = PinHole(f, cv, cx, cy, cz, p3d)
    return p2d, depth