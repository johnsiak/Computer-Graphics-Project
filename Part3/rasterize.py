import numpy as np

def rasterize(p2d, Rows, Columns, H, W):
    L = p2d.shape[0] # Number of points
    n2d = np.zeros((L, 2))
    # Scaling factors
    w_anal = Columns/W
    h_anal = Rows/H
    # Scaling
    for i in range(L):
        n2d[i, 0] = np.around((p2d[i, 0] + H/2)*h_anal) # x
        n2d[i, 1] = np.around((-p2d[i, 1] + W/2)*w_anal) # y
    return n2d