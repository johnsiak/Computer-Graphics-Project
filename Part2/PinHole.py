import numpy as np
from ChangeCoordinateSystem import *

def PinHole(f, cv, cx, cy, cz, p3d):
    #p3d is a 3xN matrix
    R = np.stack((cx, cy, cz)).T # The columns of R are the coordinates of the camera
    p3d = ChangeCoordinateSystem(p3d, R, cv) # Change from WCS to CCS
    N = p3d.shape[1]
    depth = np.zeros(N)
    x = np.zeros(N)
    y = np.zeros(N)
    for i in range(N):
        depth[i] = p3d[2,i] # z
        x[i] = f*p3d[0,i]/depth[i] # f*x/z
        y[i] = f*p3d[1,i]/depth[i] # f*y/z
    p2d = np.stack((x, y)).T # p2d is a Nx2 matrix
    return p2d, depth