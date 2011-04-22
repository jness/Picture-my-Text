#!/usr/bin/env python
import Image
import argparse
import math

# Build my Parser with help for user input
parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='File containing your text')
parser.add_argument('output_image', help='This is the name of the image')
args = parser.parse_args()

# Read in your text file
f = open(args.input_file, 'r')
message = f.read()

# Get the chr() for each of your inputed characters
barcode_data = {}
count = 0
for letter in message:
    barcode_data[count] = ord(letter)
    count += 1

# Define Image properties
characters = len(barcode_data)
width = math.ceil(math.sqrt(characters))
height = int(math.ceil(characters / width))
size = (int(width), height)

print 'characters:', characters
print 'width:', int(width)
print 'height:', height

# Create the new image object
im = Image.new('L', size) 

# just like a printer we will print a color code
# one pixel at a time
vcursor = 0
letter = 0
while vcursor < height:
    cursor = 0
    while cursor < width:
        try:
            color = barcode_data[letter]
        except KeyError:
            color = 255
        position = (cursor, vcursor)
        im.putpixel(position, color)
        cursor += 1
        letter += 1
    vcursor += 1

# Image is created, lets save it to the file
im.save(args.output_image)
