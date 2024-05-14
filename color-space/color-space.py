import cv2 as cv
import numpy as np
import os

#Set the image path here

image_name = 'cat.jpg'
sample_image = cv.imread('sample-images/' + image_name)

#grayscale Image Manipulation
def grayscale(image, output_name):
    #Specify the image to be set on grayscale
    image_grayscale=cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    
    imageSaver(image_grayscale, output_name)

#Image Channel Manipulation
def rgb(image, output_name, channel):

    #converts the image into RGB
    image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    #makes value within only the scope of (0-2)

    #0 is the Blue Channel
    #1 is the Green Channel
    #2 is the Red Channel
    channel = max(0, min(channel, 2))

    if channel == 0:
        output_name = output_name + '-' + 'Blue'
    elif channel == 1:
        output_name = output_name + '-' + 'Green'
    elif channel == 2:
        output_name = output_name + '-' + 'Red'

    height, width = image_rgb.shape[:2]

    channelImage=np.zeros((height, width,3), dtype=np.uint8)

    channelImage[:,:,channel] = image_rgb[:,:,channel]

    imageSaver(channelImage, output_name)


#Image HSV Manipulation
#It doesn't combine, you can only choose which one you can.'
def hsv(image, output_name, channel, hue, saturation, value):
    image_hsv=cv.cvtColor(image, cv.COLOR_BGR2HSV)

    #default value is 0 for an unmodified image
    if hue < 0 or hue > 180:
        hue = 0
    elif saturation < 0 or saturation > 255:
        saturation = 0
    elif value < 0 or value > 255:
        value = 0


    #Hue Channel
    if channel == 0:
        image_hsv[:,:,channel] = (image_hsv[:,:,channel] + hue) % 180
        converted_image=cv.cvtColor(image_hsv, cv.COLOR_HSV2BGR)
        output_name = output_name + '-' + 'Hue-Shifted%' + str(hue)
        imageSaver(converted_image, output_name)
    #Saturation Channel
    elif channel == 1:
        image_hsv[:,:,channel] = np.clip(image_hsv[:,:,channel] + saturation, 0, 255)
        converted_image=cv.cvtColor(image_hsv, cv.COLOR_HSV2BGR)
        output_name = output_name + '-' + 'Saturation-Shifted%' + str(saturation)
        imageSaver(converted_image, output_name)
    #Value Channel
    elif channel == 2:
        image_hsv[:,:,channel] = np.clip(image_hsv[:,:,channel] + value, 0, 255)
        converted_image=cv.cvtColor(image_hsv, cv.COLOR_HSV2BGR)
        output_name = output_name + '-' + 'Value-Shifted%' + str(value)
        imageSaver(converted_image, output_name)
    else:
        #converts the image back to default if no channel is set
        converted_image=cv.cvtColor(image_hsv, cv.COLOR_HSV2BGR)
        imageSaver(converted_image, output_name)


#just an imageSaver
def imageSaver(image_modified, output_name):
    # Specify the folder directory to save the output images
    output_folder = 'output_images'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_filename = os.path.join(output_folder,  output_name + '.jpg')
    cv.imwrite(output_filename, image_modified)

    print(f"Image Snapshot Saved '{output_filename}' in the '{output_folder}'.")


#for grayscale Channel
grayscale(sample_image, 'BW')

#for RGB channel
#sample-image-location, channel-number
rgb(sample_image, 'RGB', 5)

#for HSV channel the three values next to the channel are
#channel 0 is Hue
#channel 1 is Saturation
#channel 2 is value
#sample-image-location, channel-number , Hue(0-179), Saturation(0-255) and Value(0-255)
hsv(sample_image, 'HSV', 1, 0, 265, 0)


