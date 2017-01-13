#! /usr/local/bin/python3
# Python Challenge 12

# h: 4, w: 2

from PIL import Image, ImageFilter

im = Image.open('/Users/ares/Documents/Scripts/python/challenge/evil1.jpg','r')

new = Image.new('RGB',im.size)

im1 = im.split()

for img in im1:
    img.show()
