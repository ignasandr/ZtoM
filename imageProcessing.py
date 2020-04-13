from PIL import Image
import sys
import os

image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    imgRot = img.rotate(90)
    clean_name = os.path.splitext(filename)[0]
    imgRot.save(f'{output_folder}{clean_name}.png', 'png')
    print('done!')