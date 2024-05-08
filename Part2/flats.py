import numpy as np
from bresenham import *

def flats(canvas, vertices, vcolors):
    # Calculate the 3 edges of the triangle
    edge1 = bresenham(vertices[0], vertices[1])
    edge2 = bresenham(vertices[1], vertices[2])
    edge3 = bresenham(vertices[2], vertices[0])

    # Calculate the mean color of the vertices
    color = [0, 0, 0]
    color[0] = (vcolors[0][0] + vcolors[1][0] + vcolors[2][0])/3    #R
    color[1] = (vcolors[0][1] + vcolors[1][1] + vcolors[2][1])/3    #G
    color[2] = (vcolors[0][2] + vcolors[1][2] + vcolors[2][2])/3    #B

    updatedcanvas = canvas.copy()

    # Sorting the elements of the edges in ascending order based on the first element
    edge1 = [p for p in sorted(edge1, key=lambda l: l[0])]
    edge2 = [p for p in sorted(edge2, key=lambda l: l[0])]
    edge3 = [p for p in sorted(edge3, key=lambda l: l[0])]

    # Paint all edges
    for x, y in edge1:
        updatedcanvas[y][x] = color
    for x, y in edge2:
        updatedcanvas[y][x] = color
    for x, y in edge3:
        updatedcanvas[y][x] = color

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

            # Paint the pixels between the leftmost and rightmost active points
            for i in range(leftmost + 1, rightmost): # The active points have already been painted before (leftmost and rightmost)
                if (i, scanline) in active:
                    continue
                else:
                    updatedcanvas[i][scanline] = color

    return updatedcanvas