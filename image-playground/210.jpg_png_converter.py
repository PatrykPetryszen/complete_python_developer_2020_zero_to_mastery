import sys
import os
from PIL import Image

#grab first and second document
#jpg_png_converter.py Pokedex/ new/ so we do
image_folder = sys.argv[1]
output_folder = sys.argv[2]

print(image_folder, output_folder)

#check if new/ exists, if not create the folder
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#loop through Pokedex and convert the images to png
#save all the images to the new folder

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    img.save(f'{output_folder}{filename}.png', 'png')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done')

#We could do it without f strings:
# Image.open(image_folder + filename)
# img.save(output_folder + clean_name + '.png', 'png')