#! /usr/local/bin/python3
# Python Challenge 7

from PIL import Image
from string import ascii_lowercase

im = Image.open('/Users/ares/Documents/Scripts/python/challenge/oxygen.png')

# Crop to line
img = im.crop((0,46,608,47))

for width in range(0,img.width,7):
    w = img.getpixel((width,0))[1]
    print(chr(w), end='')

x = [105, 110, 116, 101, 103, 114, 105, 116, 121]

print("\n"+"".join([ chr(z) for z in x ]))
