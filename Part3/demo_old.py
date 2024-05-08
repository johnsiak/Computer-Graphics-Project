import numpy as np
import matplotlib.pyplot
import matplotlib.image
from RotateTranslate import *
from RenderObject import *

# Load and read data
data = np.load("h2.npy", allow_pickle=True).tolist()

p3d = np.array(data['verts3d'])
faces = np.array(data['faces'])
vcolors = np.array(data['vcolors'])
u = data['u']
cK = data['c_lookat']
cup = data['c_up']
cv = data['c_org']
t1 = data['t_1']
t2 = data['t_2']
phi = data['phi']

# Variables
cam_w = 15
cam_h = 15
img_w = 512
img_h = 512
f = 70

# Step 0
img = RenderObject(p3d, faces, vcolors, cam_h, cam_w, img_h, img_w, f, cv, cK, cup)
matplotlib.pyplot.figure(1)
matplotlib.pyplot.imshow(img)
matplotlib.pyplot.title('Step 0 - Initial picture')
matplotlib.pyplot.show()
matplotlib.image.imsave('0.jpg', np.array(img))

# Step 1
A = np.zeros((3,1)) # Assuming that A is the origin of the coordinates
p3d = RotateTranslate(p3d, 0, u, A, t1)
img = RenderObject(p3d, faces, vcolors, cam_h, cam_w, img_h, img_w, f, cv, cK, cup)
matplotlib.pyplot.figure(2)
matplotlib.pyplot.imshow(img)
matplotlib.pyplot.title('Step 1 - t1 Translation')
matplotlib.pyplot.show()
matplotlib.image.imsave('1.jpg', np.array(img))

# Step 2
t0 = np.zeros((3,1)) # No translation
p3d = RotateTranslate(p3d, phi, u, A, t0)
img = RenderObject(p3d, faces, vcolors, cam_h, cam_w, img_h, img_w, f, cv, cK, cup)
matplotlib.pyplot.figure(3)
matplotlib.pyplot.imshow(img)
matplotlib.pyplot.title('Step 2 - phi Rotation')
matplotlib.pyplot.show()
matplotlib.image.imsave('2.jpg', np.array(img))

# Step 3
p3d = RotateTranslate(p3d, 0, u, A, t2)
img = RenderObject(p3d, faces, vcolors, cam_h, cam_w, img_h, img_w, f, cv, cK, cup)
matplotlib.pyplot.figure(4)
matplotlib.pyplot.imshow(img)
matplotlib.pyplot.title('Step 3 - t2 Translation')
matplotlib.pyplot.show()
matplotlib.image.imsave('3.jpg', np.array(img))