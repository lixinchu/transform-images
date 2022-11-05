import os
import random

from os import listdir
from PIL import Image

# change: path/directory of images
folder_dir = "C:/Users/Lixin/Desktop/"

count = 0

for images in os.listdir(folder_dir):
    img = Image.open(images)
    
    # generate random angle
    rotate = random.randint(0, 36)

    # rotate image to selected angle
    output = img.rotate(rotate, expand=True)

    # save transformed image with unique name
    output.save("output_%_.png" % count)
    count +=1
