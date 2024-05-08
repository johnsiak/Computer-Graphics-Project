import numpy as np
import matplotlib.pyplot
import matplotlib.image
from render_object import *

# PhongMaterial class
class PhongMaterial:
    def __init__(self, ka: float, kd: float, ks: float, nphong: int):
        self.ka = ka
        self.kd = kd
        self.ks = ks
        self.nphong = nphong

# PointLight class
class PointLight:
    def __init__(self, pos, intensity):
        self.pos = pos
        self.intensity = intensity

# Load and read data
data = np.load("h3.npy", allow_pickle=True).tolist()
verts = np.array(data['verts'])
vertex_colors = np.array(data['vertex_colors'])
face_indices = np.array(data['face_indices'])
cam_eye = np.array(data['cam_eye'])
cam_up = np.array(data['cam_up'])
cam_lookat = np.array(data['cam_lookat'])
ka = np.array(data['ka'])
kd = np.array(data['kd'])
ks = np.array(data['ks'])
n = np.array(data['n'])
light_positions = np.array(data['light_positions'])
light_intensities = np.array(data['light_intensities'])
Ia = np.array(data['Ia'])
M = np.array(data['M'])
N = np.array(data['N'])
W = np.array(data['W'])
H = np.array(data['H'])
bg_color = np.array(data['bg_color'])
f = 70

light1 = PointLight(light_positions[0], light_intensities[0])
light2 = PointLight(light_positions[1], light_intensities[1])
light3 = PointLight(light_positions[2], light_intensities[2])
lights = [light1, light2, light3]

#Gouraud
#Full lighting
mat = PhongMaterial(ka, kd, ks, n)
img = render_object('gouraud', f, cam_eye, cam_lookat, cam_up, bg_color, M, N, H, W, verts, vertex_colors, face_indices, mat, n, lights, Ia)
matplotlib.pyplot.figure(1)
matplotlib.pyplot.imshow(img)
matplotlib.pyplot.title('Gouraud Full Lighting')
matplotlib.pyplot.show()
matplotlib.image.imsave('gouraud_full.png', np.array(img))

#Ambient Lighting
mat = PhongMaterial(ka, 0, 0, n)
img = render_object('gouraud', f, cam_eye, cam_lookat, cam_up, bg_color, M, N, H, W, verts, vertex_colors, face_indices, mat, n, lights, Ia)
matplotlib.pyplot.figure(1)
matplotlib.pyplot.imshow(img)
matplotlib.pyplot.title('Gouraud Ambient Lighting')
matplotlib.pyplot.show()
matplotlib.image.imsave('gouraud_ambient.png', np.array(img))

#Diffusion Lighting
mat = PhongMaterial(0, kd, 0, n)
img = render_object('gouraud', f, cam_eye, cam_lookat, cam_up, bg_color, M, N, H, W, verts, vertex_colors, face_indices, mat, n, lights, Ia)
matplotlib.pyplot.figure(1)
matplotlib.pyplot.imshow(img)
matplotlib.pyplot.title('Gouraud Diffusion Lighting')
matplotlib.pyplot.show()
matplotlib.image.imsave('gouraud_diffusion.png', np.array(img))

#Specular Lighting
mat = PhongMaterial(0, 0, ks, n)
img = render_object('gouraud', f, cam_eye, cam_lookat, cam_up, bg_color, M, N, H, W, verts, vertex_colors, face_indices, mat, n, lights, Ia)
matplotlib.pyplot.figure(1)
matplotlib.pyplot.imshow(img)
matplotlib.pyplot.title('Gouraud Specular Lighting')
matplotlib.pyplot.show()
matplotlib.image.imsave('gouraud_specular.png', np.array(img))


#Phong
#Full lighting
mat = PhongMaterial(ka, kd, ks, n)
img = render_object('phong', f, cam_eye, cam_lookat, cam_up, bg_color, M, N, H, W, verts, vertex_colors, face_indices, mat, n, lights, Ia)
matplotlib.pyplot.figure(1)
matplotlib.pyplot.imshow(img)
matplotlib.pyplot.title('Phong Full Lighting')
matplotlib.pyplot.show()
matplotlib.image.imsave('phong_full.png', np.array(img))

#Ambient Lighting
mat = PhongMaterial(ka, 0, 0, n)
img = render_object('phong', f, cam_eye, cam_lookat, cam_up, bg_color, M, N, H, W, verts, vertex_colors, face_indices, mat, n, lights, Ia)
matplotlib.pyplot.figure(1)
matplotlib.pyplot.imshow(img)
matplotlib.pyplot.title('Phong Ambient Lighting')
matplotlib.pyplot.show()
matplotlib.image.imsave('phong_ambient.png', np.array(img))

#Diffusion Lighting
mat = PhongMaterial(0, kd, 0, n)
img = render_object('phong', f, cam_eye, cam_lookat, cam_up, bg_color, M, N, H, W, verts, vertex_colors, face_indices, mat, n, lights, Ia)
matplotlib.pyplot.figure(1)
matplotlib.pyplot.imshow(img)
matplotlib.pyplot.title('Phong Diffusion Lighting')
matplotlib.pyplot.show()
matplotlib.image.imsave('phong_diffusion.png', np.array(img))

#Specular Lighting
mat = PhongMaterial(0, 0, ks, n)
img = render_object('phong', f, cam_eye, cam_lookat, cam_up, bg_color, M, N, H, W, verts, vertex_colors, face_indices, mat, n, lights, Ia)
matplotlib.pyplot.figure(1)
matplotlib.pyplot.imshow(img)
matplotlib.pyplot.title('Phong Specular Lighting')
matplotlib.pyplot.show()
matplotlib.image.imsave('phong_specular.png', np.array(img))
