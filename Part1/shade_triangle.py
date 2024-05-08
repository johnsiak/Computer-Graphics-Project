from flats import *
from Gourauds import *

def shade_triangle(canvas, vertices, vcolors, shade_t):
    # Call the flats or Gouraud function based on the shade_t input
    if shade_t == "flat":
        updatedcanvas = flats(canvas, vertices, vcolors)
    elif shade_t == "gouraud":
        updatedcanvas = Gourauds(canvas, vertices, vcolors)
    else:
        print("Error: shade_t must be ""flat"" or ""gouraud""")
    return updatedcanvas