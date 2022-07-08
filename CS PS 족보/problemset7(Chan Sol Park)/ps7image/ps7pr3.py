#
# ps7pr3.py (Problem Set 7, Problem 3)
#
# Image processing with loops and image objects
#
# Computer Science 111
# 

from cs111png import *

def invert(filename):
    """ loads a PNG image from the file with the specified filename
        and creates a new image in which the colors of the pixels are
        inverted.
        input: filename is a string specifying the name of the PNG file
               that the function should process.
        No value is returned, but the new image is stored in a file
        whose name is invert_filename, where filename is the name of
        the original file.
    """
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()

    # process the image, one pixel at a time
    for r in range(height):
        for c in range(width):
            # get the RGB values of the pixel at row r, column c
            rgb = img.get_pixel(r, c)            
            red = rgb[0]
            green = rgb[1]
            blue = rgb[2]

            # invert the colors of the pixel at row r, column c
            new_rgb = [255 - red, 255 - green, 255 - blue]
            img.set_pixel(r, c, new_rgb)

    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'invert_' + filename
    img.save(new_filename)

def brightness(rgb):
    """ takes the RGB values of a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    return (21*red + 72*green + 7*blue) // 100

### PUT YOUR WORK FOR PROBLEM 3 BELOW. ###

def bw(filename, threshold):
    """gets an image name and a threshold value and createa new image that is
       a black and white version of the original value.
    """
    img = load_image(filename)
    height = img.get_height()
    width = img.get_width()
    for r in range(height):
        for c in range(width):
            rgb = img.get_pixel(r,c)
            bright = brightness(rgb)
            if bright > threshold:
                new_rgb = [255, 255, 255]
                img.set_pixel(r, c, new_rgb)
            else:
                new_rgb = [0, 0, 0]
                img.set_pixel(r, c, new_rgb)
    new_filename = 'bw_' + filename
    img.save(new_filename)

def mirror_vert(filename):
    """gets an image name and create a new image in which the original image
       is mirrored vertically.
    """
    img = load_image(filename)
    height = img.get_height()
    width = img.get_width()
    mid_width = width//2
    for r in range(height):
        for c in range(mid_width):
            rgb = img.get_pixel(r,c)
            new_c = width - 1 - c
            img.set_pixel(r, new_c, rgb)
    new_filename = 'mirror_vert' + filename
    img.save(new_filename)

def extract(filename, rmin, rmax, cmin, cmax):
    """gets an image name and 4 points and extracts a portion of the original
       image that is specified by the points.
    """
    img = load_image(filename)
    height = img.get_height()
    width = img.get_width()
    new_height = rmax - rmin
    new_width = cmax - cmin
    new_img = Image(new_height, new_width)
    for x in range(new_height):
        for y in range(new_width):
            rgb = img.get_pixel(x+rmin, y+cmin)
            new.img_set_pixel(x, y, rgb)
    new_filename = 'extract_' + filename
    new_img.save(new_filename)
            
            
