import os
import skimage.io
import skimage.filters
import matplotlib.pyplot as plt

from os import listdir, truncate

# change: path/directory of images
folder_dir = "C:/Users/Lixin/Desktop/"

count = 0
sigma = 3.0

for images in os.listdir(folder_dir):
    image = skimage.io.imread(images)

    # display original image
    fig, ax = plt.subplots()
    plt.imshow(image)
    
    # apply gaussian blur, creating a new image
    blurred = skimage.filters.gaussian(
        image, sigma=(sigma,sigma), truncate=3.5, channel_axis=2)

    # display blurred image
    fig, ax = plt.subplots()
    plt.imshow(blurred)

    # save blurred image
    skimage.io.imsave("blurred_%_.png" % count)
    count += 1
