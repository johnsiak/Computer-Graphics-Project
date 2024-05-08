def bresenham(vertex1, vertex2):
    x1, y1 = vertex1
    x2, y2 = vertex2
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # Swap coordinates if slope is greater than 1
    swap = dy > dx
    if swap:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        dx, dy = dy, dx

    x, y = x1, y1
    p = 2*dy - dx
    # Starting point
    edge = [[x, y]] if not swap else [[y, x]]

    while x != x2 or y != y2: # Until we get to the final point.
        if p > 0:
            # If p > 0, move up/down one pixel
            y += 1 if y < y2 else -1
            p += 2*(dy - dx)
        else:
            p += 2*dy
        # move right/left one pixel
        x += 1 if x < x2 else -1
        edge.append([x, y] if not swap else [y, x])
    return edge