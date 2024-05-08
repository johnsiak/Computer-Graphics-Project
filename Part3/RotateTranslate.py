from rotmat import *
import numpy as np

def RotateTranslate(cp, theta, u, A, t):
    u = np.array(u)/np.linalg.norm(u) # Normalise vector
    cp = cp - A # Change coordinates by moving the centre to A
    R = rotmat(theta, u)
    N = cp.shape[1] # Number of points
    cq = np.zeros((3, N))
    # Rotate each point
    for i in range(N):
        cq[:,i] = np.dot(R, cp[:,i])
    cq = cq + A # Change coordinates by moving the centre to the original point     
    cq = cq + t.reshape(3,1) # Translation
    return cq