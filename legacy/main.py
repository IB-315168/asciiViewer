from PIL import ImageEnhance, ImageGrab
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
            if x <= 21:
                image[a][b] = str("@")
            if 21 < x <= 42:
                image[a][b] = str("$")
            if 42 < x <= 63:
                image[a][b] = str("#")
            if 63 < x <= 84:
                image[a][b] = str("*")
            if 84 < x <= 105:
                image[a][b] = str("!")
            if 105 < x <= 126:
                image[a][b] = str("=")
            if 126 < x <= 147:
                image[a][b] = str(";")
            if 147 < x <= 168:
                image[a][b] = str(":")
            if 168 < x <= 189:
                image[a][b] = str("~")
            if 189 < x <= 210:
                image[a][b] = str("-")
            if 210 < x <= 231:
                image[a][b] = str(",")
            if 231 < x <= 252:
                image[a][b] = str(".")
            if 252 < x:
                image[a][b] = str(" ")

    line = ""
    for x in range(img.height):
        for y in range(img.width):
            line = line + (image[x][y])
        print(line)
        line = ""


while True:
    screencap()
