from shade_triangle import *

def render(verts2d, faces, vcolors, depth, shade_t):
    # Initialize an empty image with a white background (M x N x 3)
    M = 512
    N = 512
    img = [[[1.0 for _ in range(3)] for _ in range(N)] for _ in range(M)]

    depths = []
    colors = []
    for triangle in faces:
        index = faces.index(triangle)
        # Replace the vertex indices with their coordinates
        faces[index] = [verts2d[triangle[0]], verts2d[triangle[1]], verts2d[triangle[2]]]

        # Calculate the average depth of the vertices for each face
        average_depth = (depth[triangle[0]] + depth[triangle[1]] + depth[triangle[2]])/3
        depths.append(average_depth)
        # Calculate the color of each vertex for every face
        colors.append([vcolors[triangle[0]], vcolors[triangle[1]], vcolors[triangle[2]]])
    
    # Sort the faces based on depth from farthest to closest
    triangles = [(depths[i], faces[i], colors[i]) for i in range(len(faces))]
    triangles.sort(key=lambda l: -l[0])
    depths = [k[0] for k in triangles]
    faces = [k[1] for k in triangles]
    colors = [k[2] for k in triangles]
    
    # Call shade_triangle
    for triangle in faces:
        img = shade_triangle(img, triangle, colors[faces.index(triangle)], shade_t)

    return img