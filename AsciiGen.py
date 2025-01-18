from PIL import Image, ImageDraw, ImageFont

import math, random, os, Photos

chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|1?-_+~<>i!lI;:,^`\'."[::-1]

charArray = list(chars)
charLength = len(charArray)
interval = charLength/256


oneCharWidth = 8
oneCharHeight = 18

def getchar(inputInt):
    return charArray[math.floor(inputInt*interval)]

text_file = open("output.txt", "w")

randimg = random.choice(os.listdir('Photos'))

im = Image.open(os.path.join('Photos', randimg))

width, height = im.size
ScaleFactor = 0.2
im = im.resize((int(ScaleFactor*width), int(ScaleFactor*height*(oneCharWidth/oneCharHeight))), Image.NEAREST)
width, height = im.size
pix = im.load()

outputImg = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color = (0,0,0))
d = ImageDraw.Draw(outputImg)

for i in range(height):
    for j in range(width):
        r, g, b = pix[j, i]
        h = int(r/3 + g/3 + b/3)
        pix[j, i] = (h,h,h)
        text_file.write(getchar(h))
        d.text((j*oneCharWidth, i*oneCharHeight), getchar(h), fill = (r, g, b))

    text_file.write('\n')

outputImg.save("output.png")