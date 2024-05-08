import numpy as np

def calculate_normals(verts, faces):
    Nu = verts.shape[1]
    NT = faces.shape[1]
    normals = np.zeros((3, Nu))

    # Calculate the normals for each triangle
    for k in range(NT):
        # Get the indices of the vertices for the current triangle
        index = faces[:, k]

        # Get the coordinates of the vertices for the current triangle
        v1 = verts[:, index[0]]
        v2 = verts[:, index[1]]
        v3 = verts[:, index[2]]

        # Calculate the normal vector for the current triangle
        normal = np.cross(v1 - v2, v1 - v3) #ABxAC

        # Add the normal vector to the vertices of the triangle
        normals[:, index[0]] += normal
        normals[:, index[1]] += normal
        normals[:, index[2]] += normal

    # Normalise the normals
    normals = normals/np.linalg.norm(normals, axis=0)
    
    return normals