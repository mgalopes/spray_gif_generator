from PIL import Image
import os

def create_gif(input_folder, output_gif, duration):
    # Get all image files from the folder
    images = [img for img in os.listdir(input_folder) if img.endswith((".png", ".jpg", ".jpeg", ".bmp"))]
    images.sort()  # Sort images by name

    # Load images into a list
    frames = [Image.open(os.path.join(input_folder, img)) for img in images]

    # Save as GIF
    frames[0].save(output_gif, save_all=True, append_images=frames[1:], optimize=False, duration=duration, loop=0)

# Parameters
input_folder = 'C:/Users/garci/Documents/Lab spray dynamics/ROTA_2030/cvcc/GASOLINA_14/Mean_'  # Replace with the path to your folder
output_gif = 'GASOLINA_14.gif'  # Name of the output GIF file
duration = 500  # Duration between frames in milliseconds

create_gif(input_folder, output_gif, duration)