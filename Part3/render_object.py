from calculate_normals import *
from CameraLookingAt import *
from rasterize import *
from shade_gouraud import *
from shade_phong import *

def render_object(shader, focal, eye, 
                  lookat, up, bg_color,
                  M, N, H, W,
                  verts, vert_colors, faces,
                  mat, n, lights, light_amb):
    normals = calculate_normals(verts, faces)
    p2d, depth = CameraLookingAt(focal, eye, lookat, up, verts)
    p2d = rasterize(p2d, M, N, H, W)
    p2d = np.array(p2d).astype(int) # Pixels are integers

    verts = verts.T
    faces = faces.T
    vert_colors = vert_colors.T
    normals = normals.T

    p2d = p2d.tolist()
    faces = faces.tolist()
    vert_colors = vert_colors.tolist()
    depth = depth.tolist()
    normals = normals.tolist()

    depths = []
    colors = []
    bcoords = []
    normals_new = []
    p3d = []

    index = 0
    for triangle in faces:
        # Replace the vertex indices with their coordinates
        faces[index] = [p2d[triangle[0]], p2d[triangle[1]], p2d[triangle[2]]]
        # Create list of 3D coordinates of the vertices to calculate the bcoord
        p3d.append([verts[triangle[0]], verts[triangle[1]], verts[triangle[2]]])
        # Calculate the average depth of the vertices for each face
        average_depth = (depth[triangle[0]] + depth[triangle[1]] + depth[triangle[2]])/3
        depths.append(average_depth)
        # Calculate the color and normal vectors of each vertex for every triangle
        colors.append([vert_colors[triangle[0]], vert_colors[triangle[1]], vert_colors[triangle[2]]])
        normals_new.append([normals[triangle[0]], normals[triangle[1]], normals[triangle[2]]])
        # Calculate the bcoord (mean of the 3D vertices)
        bcoords.append(np.mean(p3d[index], axis = 1))
        index += 1
    
    # Sort the faces based on depth from closest to farthest
    triangles = [(depths[i], faces[i], colors[i], bcoords[i], normals_new[i]) for i in range(len(faces))]
    triangles.sort(key=lambda l: l[0])
    depths = [k[0] for k in triangles]
    faces = [k[1] for k in triangles]
    colors = [k[2] for k in triangles]
    bcoords = [k[3] for k in triangles]
    normals = [k[4] for k in triangles]

    X = [[[bg_color[i] for i in range(3)] for _ in range(N)] for _ in range(M)]
    if shader == 'gouraud':
        for k in range(len(faces)):
            X = shade_gouraud(faces[k], normals[k], colors[k], bcoords[k], eye, mat, lights, light_amb, X)
    elif shader == 'phong':
        for k in range(len(faces)):
            X = shade_phong(faces[k], normals[k], colors[k], bcoords[k], eye, mat, lights, light_amb, X)
    return X
