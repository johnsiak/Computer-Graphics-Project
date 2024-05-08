import numpy as np

def ChangeCoordinateSystem(cp, R, c0):
    N = cp.shape[1]
    dp = np.zeros((3, N))
    # Change coordinate system for each point
    for i in range(N):
        dp[:,i] = np.dot(R.T, cp[:,i] - c0)
    return dp