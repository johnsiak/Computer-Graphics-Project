import numpy as np

def interpolate_vectors(p1, p2, V1, V2, xy, dim):
    if dim == 1:
        if(p2[0] - p1[0] == 0):
            return V1
        else:
            # x axis
            lamda = (p2[0] - xy)/(p2[0] - p1[0])
    elif dim == 2:
        if(p2[1] - p1[1] == 0):
            return V1
        else:
            # y axis
            lamda = (p2[1] - xy)/(p2[1] - p1[1])
    else:
        print("Error: dim must be 1 or 2")

    V = lamda*np.array(V1) + (1-lamda)*np.array(V2)
    return V