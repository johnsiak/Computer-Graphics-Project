from light import *
from bresenham import *
from interpolate_vectors import *

def shade_gouraud(vertsp, vertsn, vertsc, bcoords, cam_pos, mat, lights, light_amb, X):
    # Lighting on vertices
    vertsc[0] = light(bcoords, vertsn[0], vertsc[0], cam_pos, mat, lights, light_amb)
    vertsc[1] = light(bcoords, vertsn[1], vertsc[1], cam_pos, mat, lights, light_amb)
    vertsc[2] = light(bcoords, vertsn[2], vertsc[2], cam_pos, mat, lights, light_amb)
    
    vcolors = vertsc
    vertices = vertsp

    # Calculate the 3 edges of the triangle
    edge1 = bresenham(vertices[0], vertices[1])
    edge2 = bresenham(vertices[1], vertices[2])
    edge3 = bresenham(vertices[2], vertices[0])

    updatedcanvas = X.copy()

    # Sorting the elements of the edges in ascending order based on the first element
    edge1 = [p for p in sorted(edge1, key=lambda l: l[0])]
    edge2 = [p for p in sorted(edge2, key=lambda l: l[0])]
    edge3 = [p for p in sorted(edge3, key=lambda l: l[0])]

    for p1 in edge1:
        if p1 not in vertices:
            if abs(vertices[0][0] - vertices[1][0]) > abs(vertices[0][1] - vertices[1][1]):
                updatedcanvas[p1[1]][p1[0]] = interpolate_vectors(vertices[0], vertices[1], vcolors[0],
                                                                vcolors[1], p1[0], 1) # x axis interpolation
            else:
                updatedcanvas[p1[1]][p1[0]] = interpolate_vectors(vertices[0], vertices[1], vcolors[0],
                                                                    vcolors[1], p1[1], 2) # y axis interpolation
        else:
            # The current pixel is a vertex, so we use the corresponding color value
            index = vertices.index(p1)
            updatedcanvas[p1[1]][p1[0]] = vcolors[index]

    for p2 in edge2:
        if p2 not in vertices:
            if abs(vertices[1][0] - vertices[2][0]) > abs(vertices[1][1] - vertices[2][1]):
                updatedcanvas[p2[1]][p2[0]] = interpolate_vectors(vertices[1], vertices[2], vcolors[1],
                                                                    vcolors[2], p2[0], 1) # x axis interpolation
            else:
                updatedcanvas[p2[1]][p2[0]] = interpolate_vectors(vertices[1], vertices[2], vcolors[1],
                                                                vcolors[2], p2[1], 2) # y axis interpolation
        else:
            # The current pixel is a vertex, so we use the corresponding color value
            index = vertices.index(p2)
            updatedcanvas[p2[1]][p2[0]] = vcolors[index]

    for p3 in edge3:
        if p3 not in vertices:
            if abs(vertices[2][0] - vertices[0][0]) > abs(vertices[2][1] - vertices[0][1]):
                updatedcanvas[p3[1]][p3[0]] = interpolate_vectors(vertices[2], vertices[0], vcolors[2],
                                                                vcolors[0],  p3[0], 1) # x axis interpolation
            else:
                updatedcanvas[p3[1]][p3[0]] = interpolate_vectors(vertices[2], vertices[0], vcolors[2],
                                                                vcolors[0], p3[1], 2) # y axis interpolation
        else:
            # The current pixel is a vertex, so we use the corresponding color value
            index = vertices.index(p3)
            updatedcanvas[p3[1]][p3[0]] = vcolors[index]

    # Calculate the bottom and top scanlines of the triangle
    bottom = min(edge1[0][0], edge2[0][0], edge3[0][0])
    top = max(edge1[-1][0], edge2[-1][0], edge3[-1][0])

    # Find the active points on each scanline and fill in the pixels between them
    for scanline in range(bottom, top + 1):
        # Find the active points on the current scanline
        active = []
        for p1 in edge1:
            if p1[0] == scanline:
                active.append(p1)
        for p2 in edge2:
            if p2[0] == scanline:
                active.append(p2)
        for p3 in edge3:
            if p3[0] == scanline:
                active.append(p3)

        # If there is only one active point, skip to the next scanline
        if len(active) == 1:
            continue
        else:
            # Find the leftmost and rightmost active points
            leftmost = np.array(active).min(axis=0)[1]
            rightmost = np.array(active).max(axis=0)[1]

            # Fill in the pixels between the leftmost and rightmost active points
            for i in range(leftmost + 1, rightmost): # The active points have already been painted before (leftmost and rightmost)
                if [i, scanline] in active:
                    continue
                else:
                    updatedcanvas[i][scanline] = interpolate_vectors((leftmost, scanline), (rightmost, scanline), 
                                                                            updatedcanvas[leftmost][scanline], updatedcanvas[rightmost][scanline], 
                                                                            i, 1) # x axis interpolation
    Y = updatedcanvas
    return Y
