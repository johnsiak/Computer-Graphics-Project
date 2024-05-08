import numpy as np

def rotmat(theta, u):
    R = np.array([[(1 - np.cos(theta))*u[0]**2 + np.cos(theta),
                      (1 - np.cos(theta))*u[0]*u[1] - np.sin(theta)*u[2],
                      (1 - np.cos(theta))*u[0]*u[2] + np.sin(theta)*u[1]],
                      [(1 - np.cos(theta))*u[0]*u[1] - np.sin(theta)*u[2],
                       (1 - np.cos(theta))*u[1]**2 + np.cos(theta),
                      (1 - np.cos(theta))*u[1]*u[2] - np.sin(theta)*u[0]],
                      [(1 - np.cos(theta))*u[0]*u[2] + np.sin(theta)*u[1],
                       (1 - np.cos(theta))*u[1]*u[2] - np.sin(theta)*u[0],
                       (1 - np.cos(theta))*u[2]**2 + np.cos(theta)]])
    return R.T # R Transpose because we rotate clockwise