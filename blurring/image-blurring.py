import cv2 as cv
import numpy as np
import os


image_name = 'cat.jpg'
sample_image = cv.imread('sample-images/' + image_name)

#Blurs the image between 0 - 100, The value of blurrification
#Depends Heavily on its KSize Value
def imageBlur(image, ksize, output_name):
    # ksize 
    if ksize < 1 or ksize > 100:
        ksize = 1
        output_name = 'default'
    else:
        blurValue = (ksize, ksize)
        image = cv.blur(image, blurValue)
        output_name = output_name + '-%' + str(ksize)
    
    imageSaver(image, output_name)



def imageSaver(image_modified, output_name):
    # Specify the folder directory to save the output images
    output_folder = 'output_images'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_filename = os.path.join(output_folder,  output_name + '.jpg')
    cv.imwrite(output_filename, image_modified)

    print(f"Image Snapshot Saved '{output_filename}' in the '{output_folder}'.")

imageBlur(sample_image, -150, 'Blurred')