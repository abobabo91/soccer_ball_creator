from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Map the image's triangular section to one quarter of the sphere's top half
def map_triangle_to_sphere(image, pixels=20, sides=4):
    # Ensure the image is in RGB format
    image = image.convert("RGB")
    texture_array = np.array(image)
    height, width, _ = texture_array.shape

    # Define the triangular region of the image to use
    start_x, end_x = 0, width
    start_y, end_y = 0, height

    triangular_region = texture_array[start_y:end_y, start_x:end_x]

    # Sphere coordinates for one quarter of the top half
    rows, cols, _ = triangular_region.shape
    u = np.linspace(0, np.pi / 2, cols)  # Quarter of the top half
    v = np.linspace(0, np.pi / 2, rows)
    u, v = np.meshgrid(u, v)
    x = np.sin(v) * np.cos(u)
    y = np.sin(v) * np.sin(u)
    z = np.cos(v)

    # Normalize triangular region to match sphere dimensions
    fcolors = triangular_region / 255

    # Map the triangular region texture onto the sphere
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    for i in range(2):  # Top and bottom halves
        for j in range(sides):  # Four quarters per hemisphere
            angle = j * np.pi * 2 / sides
            x_rot = x * np.cos(angle) - y * np.sin(angle)
            y_rot = x * np.sin(angle) + y * np.cos(angle)
            z_rot = z if i == 0 else -z
            if j % 2 == 1:
                fcolors_to_plot = fcolors
            else:
                fcolors_to_plot = fcolors[:,::-1]
            ax.plot_surface(x_rot, y_rot, z_rot, rstride=pixels, cstride=pixels, facecolors=fcolors_to_plot, linewidth=0, antialiased=False)
                
    ax.set_axis_off()
    plt.show()


if __name__ == "__main__":
    image = Image.open('input_example.jpg')
    map_triangle_to_sphere(image, pixels=1)
