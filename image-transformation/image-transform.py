import cv2 as cv
import os

image_name = 'cat.jpg'
sample_image = cv.imread('sample-images/' + image_name)

#image Reflection
#the process of flipping an Image Vertically or Horizontally.

def imageReflect(image, image_name, value):

    if value == 0:
        image_reflect = image
        image_name = 'default'
    elif value == 1:
        image_reflect = cv.flip(image, 0)
        image_name = image_name + '-vertical'
    elif value == 2:
        image_reflect = cv.flip(image, 1)
        image_name = image_name + '-Horizontal'
    elif value == 3:
        image_reflect = cv.flip(image, -1)
        image_name = image_name + '-vertical+Horizontal'
    else:
        image_reflect = image
        image_name = 'default'

    imageSaver(image_reflect, image_name)

#image Scaling
#the process of scaling an image to shrinking or expanding

def imageScale(image, image_name, scaleValue, interpolation):


    if scaleValue < 0.1 or scaleValue > 5:
        scaleValue = 1

    if interpolation == 0:
        imageScale = cv.resize(image, 
                                None, 
                                fx=scaleValue, 
                                fy=scaleValue, 
                                interpolation=cv.INTER_LINEAR)
        image_name = image_name + '-Linear'
    elif interpolation == 1:
        imageScale = cv.resize(image, 
                                None, 
                                fx=scaleValue, 
                                fy=scaleValue, 
                                interpolation=cv.INTER_NEAREST)
        image_name = image_name + '-Nearest'
    elif interpolation == 2:
        imageScale = cv.resize(image,
                                None,
                                fx=scaleValue,
                                fy=scaleValue,
                                interpolation=cv.INTER_CUBIC)
        image_name = image_name + '-Cubic'
    elif interpolation == 3:
        imageScale = cv.resize(image, 
                                None, 
                                fx=scaleValue, 
                                fy=scaleValue, 
                                interpolation=cv.INTER_LANCZOS4)
        image_name = image_name + '-Lanczos4'
    else:
        imageScale = cv.resize(image, 
                                None, 
                                fx=scaleValue, 
                                fy=scaleValue, 
                                interpolation=cv.INTER_LINEAR)
        image_name = image_name + '-Linear'


    print(imageScale.shape)
    imageSaver(imageScale, image_name)

#just an imageSaverS
def imageSaver(image_modified, output_name):
    # Specify the folder directory to save the output images
    output_folder = 'output_images'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_filename = os.path.join(output_folder,  output_name + '.jpg')
    cv.imwrite(output_filename, image_modified)

    print(f"Image Snapshot Saved '{output_filename}' in the '{output_folder}'.")

#if val is 0, no changes will be made
#if val is 1 image will be flipped vertically
#if val is 2 image will be flipped horizontally
#if val is 3 image will be flipped vertically and Horizontally
#if val exceeds the values mentioned it will be set to 0

imageReflect(sample_image, 'reflect', -1)

#scalevalue I.e if scalevalue is 0.5
#then image is reduced by its half
#scalevalue I.e if scalevalue is 2
#then image is increased its twice its size.
#the value will is set to float params
#meaning it would limit to 0.1 between 5 Only
    
#interpolation parameters
#0 Bilinear Interpolation Approach
#1 Nearest Neighbor Approach
#2 Bicubic Interpolation Approach
#3 Lanczos Interpolation Approach
    
imageScale(sample_image, 'resize', 3, 2)