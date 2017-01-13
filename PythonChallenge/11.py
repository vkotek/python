#! /usr/local/bin/python3
# Python Challenge 11

from PIL import Image, ImageOps

img = "/Users/ares/Documents/Scripts/python/challenge/cave.jpg"

ImageOps.invert(Image.open(img,'r')).show()

im = Image.open(img,'r')

dark = Image.new('RGB',im.size)

for height in range(im.height):
    for width in range(im.width):
        xy = (width, height)
        if height % 2 == 1 and width % 2 == 1:
            dark.putpixel(xy,im.getpixel(xy))
        elif height % 2 == 0 and width % 2 == 0:
            dark.putpixel(xy,im.getpixel(xy))
