import numpy as np
import matplotlib.pyplot as plt

# takes an RGB image (three dimensional array) 
# returns a two dimensional gray-scale image
#
# uses RGB to grayscale conversion formula
# 0.2126 * r + 0.7152  * g + 0.0722  * b
def to_grayscale(image):
    print(image.shape) # (368, 640, 3)
    
    # making a copy to not mess the original
    img_copy = image.copy()
    
    r, g, b = img_copy[:, :, 0], img_copy[:, :, 1], img_copy[:, :, 2]
    imgGrey = 0.2126 * r + 0.7152 * g + 0.0722 * b

    return imgGrey

#### All three functions below ####
# get a three dimensional array as a parameter
# return a three dimensional arrays

def to_red(img):
    red_img = img.copy()
    red_img[:, :, 1:] = 0
    return red_img
    
def to_green(img): 
    green_img = img.copy()
    green_img[:, :, (0,2)] = 0
    return green_img
    
def to_blue(img):
    blue_img = img.copy()
    blue_img[:, :,0:2] = 0
    return blue_img

def main():
    image = plt.imread("src/painting.png")
    grey_image = to_grayscale(image)

    # Plotting the grey-scaled image
    plt.imshow(grey_image, cmap='gray')
    fig, ax = plt.subplots(1, 3)
    ax[0].imshow(to_red(image))
    ax[1].imshow(to_green(image))
    ax[2].imshow(to_blue(image))
    plt.show()

if __name__ == "__main__":
    main()
