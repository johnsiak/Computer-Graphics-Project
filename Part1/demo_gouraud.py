import numpy as np
import matplotlib.pyplot
import matplotlib.image
from render import *

# Load and read data
data = np.load('h1.npy', allow_pickle=True)
vcolors = data[()]['vcolors'].tolist()
faces = data[()]['faces'].tolist()
depth = data[()]['depth'].tolist()
verts2d = data[()]['verts2d'].astype(int).tolist()

# Call render
img = render(verts2d, faces, vcolors, depth, "gouraud")

matplotlib.pyplot.imshow(img)
matplotlib.pyplot.title("Gouraud")
matplotlib.pyplot.show()
matplotlib.image.imsave('demo_gouraud_output.png', np.array(img))