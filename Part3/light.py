import numpy as np

# Lighting function
def light(point, normal, vcolor, cam_pos, mat, lights, light_amb):
    # Ambient lighting
    ambient = mat.ka*light_amb

    # Diffuse lighting
    diffuse = 0
    for lighter in lights:
        SP = lighter.pos - point
        L = SP/np.linalg.norm(SP)  # Normalise light direction
        diffuse += lighter.intensity*mat.kd*np.dot(normal, L)

    # Specular lighting
    specular = 0
    for lighter in lights:
        CP = cam_pos - point
        V = CP/np.linalg.norm(CP) # Normalise camera direction
        SP = lighter.pos - point
        L = SP/np.linalg.norm(SP) # Normalise light direction
        normal = np.array(normal)  # Convert normal to numpy array
        L = np.array(L)  # Convert L to numpy array
        R = 2*np.dot(normal, L)*normal - L
        specular += lighter.intensity*mat.ks*(np.dot(R, V)**mat.nphong)

    I = (diffuse + specular)*vcolor + ambient
    I = np.clip(I, 0, 1) # Clip values lower than 0 and over 1
    return I
