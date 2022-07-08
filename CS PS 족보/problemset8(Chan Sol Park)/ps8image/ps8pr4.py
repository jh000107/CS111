#
# ps8pr4.py (Problem Set 8, Problem 4)
#
# Images as 2-D lists
#
# Computer Science 111
# 

from hmcpng import *

def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels have the RGB values
        given by pixel
        inputs: height and width are non-negative integers
                pixel is a 1-D list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    pixels = []
    
    for r in range(height):
        row = [pixel] * width
        pixels += [row]

    return pixels

def blank_image(height, width):
    """creates and returns a 2-D list of pixels with ehight rows and width
       columns in which all of the pixels are green."""
    
    pixel = [0,255,0]
    return create_uniform_image(height, width, pixel)

def flip_vert(pixels):
    """gets the 2-D list pixels of an image and return the vertically flipped
       image of it. """
    height = len(pixels)
    width = len(pixels[0])
    new_image = create_uniform_image(height, width, pixels)
    for r in range(height):
        for c in range(width):
            rgb = pixels[r][c]
            new_image[height-r-1][c] = rgb
    return new_image

def reduce(pixels):
    """gets the 2-D list pixels of an image and return a new 2-D list that
       represents an image that is half the size of the original image."""
    height = len(pixels)//2
    width = len(pixels[0])//2
    new_image = create_uniform_image(width, height, pixels)
    for r in range(len(pixels)):
        for c in range(len(pixels[0])):
            new_image[r//2][c//2] = pixels[r][c]
    return new_image

def transpose(pixels):
    """takes the 2-D list pixels containing pixels for an image, and that
       creates and returns a new 2-D list that is the transpose of pixels.
    """
    height = len(pixels)
    width = len(pixels[0])
    new_image = create_uniform_image(width, height, pixels)
    for r in range(width):
        for c in range(height):
            new_image[r][c] = pixels[c][r]
    return new_image
    
def rotate_counter_clockwise(pixels):
    """take a 2-D list pixels containing pixels for an image, and create
       and return a new 2-D list of pixels for an image that is a counter
       clockwise rotation of the original image.
    """
    height = len(pixels)
    width = len(pixels[0])
    new_image = create_uniform_image(width, height, pixels)
    for r in range(width):
        for c in range(height):
            new_image[width-r-1][c] = pixels[c][r]
    return new_image

def rotate_clockwise(pixels):
    """take a 2-D list pixels containing pixels for an image, and create
       and return a new 2-D list of pixels for an image that is a clockwise
       rotation of the original image.
    """
    height = len(pixels)
    width = len(pixels[0])
    new_image = create_uniform_image(width, height, pixels)
    for r in range(width):
        for c in range(height):
            new_image[r][height-c-1] = pixels[c][r]
    return new_image
