from PIL import Image, ImageEnhance, ImageGrab
import numpy
from numpy import asarray

def screencap():
    imx = ImageGrab.grab(bbox=(118, 154, 1280, 800))
    im = imx.resize((170, 80))
    ime = ImageEnhance.Contrast(im)
    img = ime.enhance(4.0)
    data = asarray(img)
    new_data = []
    for i in data:
        for j in i:
            new_data.append(j[0])

    result = numpy.zeros((img.height, img.width))
    a = 0
    b = 0

    for i in new_data:
        if b == img.width:
            b = 0
            a = a + 1
        result[a][b] = i
        b = b + 1

    image = list(map(list, result))
    for a in range(img.height):
        for b in range(img.width):
            x = int(result[a][b])
            if x <= 3:
                image[a][b] = str(" ")
            if 3 < x <= 24:
                image[a][b] = str(".")
            if 24 < x <= 45:
                image[a][b] = str(",")
            if 45 < x <= 66:
                image[a][b] = str("-")
            if 66 < x <= 87:
                image[a][b] = str("~")
            if 87 < x <= 108:
                image[a][b] = str(":")
            if 108 < x <= 129:
                image[a][b] = str(";")
            if 129 < x <= 150:
                image[a][b] = str("=")
            if 150 < x <= 171:
                image[a][b] = str("!")
            if 171 < x <= 192:
                image[a][b] = str("*")
            if 192 < x <= 213:
                image[a][b] = str("#")
            if 213 < x <= 234:
                image[a][b] = str("$")
            if 234 < x <= 255:
                image[a][b] = str("@")

    line = ""
    for x in range (img.height):
        for y in range (img.width):
            line = line + (image[x][y])
        print(line)
        line = ""

while True:
    screencap()
