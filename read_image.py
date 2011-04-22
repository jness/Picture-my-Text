#!/usr/bin/env python
import Image
import argparse

# Build my Parser with help for user input
parser = argparse.ArgumentParser()
parser.add_argument('filename', help='This is the name of the image')
args = parser.parse_args()

# Load our image
im = Image.open(args.filename)
width = im.size[0]
height = im.size[1]

# Extract the color codes
string = ''
vcursor = 0
while vcursor < height:
    cursor = 0
    while cursor < width:
        color = im.getpixel((cursor, vcursor))
        if color != 255:
            string = string + chr(color)
        else:
            break
        cursor += 1
    vcursor += 1

# Print out the message
print string
