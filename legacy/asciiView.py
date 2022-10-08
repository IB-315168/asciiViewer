from PIL import Image, ImageEnhance, ImageGrab
from numpy import asarray


class AsciiView:
    x1, y1, x2, y2 = 0, 0, 0, 0

    def __init__(self):
        self.__run = True
        self.__listeners = []
        self.__img_print = [""] * 80

    def add_listener(self, listener):
        self.__listeners.append(listener)

    def remove_listener(self, listener):
        self.__listeners.remove(listener)

    def fire(self):
        for listener in self.__listeners:
            listener(self.__img_print)

    def setBBox(self, pos):
        self.x1 = pos[0]
        self.y1 = pos[1]
        self.x2 = pos[2]
        self.y2 = pos[3]

    def screencap(self):
        while self.__run:
            # imx = ImageGrab.grab(bbox=(118, 154, 1280, 800))

            # Prepare image
            imx = ImageGrab.grab(bbox=(self.x1, self.y1, self.x2, self.y2))
            im = imx.resize((170, 80))
            ime = ImageEnhance.Contrast(im)
            img = ime.enhance(4.0)

            # Convert image to array
            data = asarray(img)

            # new_data = []
            # for i in data:
            #     for j in i:
            #         new_data.append(j[0])
            #
            # # create populate array result with zeros
            # result = numpy.zeros((img.height, img.width))
            # a = 0
            # b = 0
            #
            # for i in new_data:
            #     if b == img.width:
            #         b = 0
            #         a = a + 1
            #     result[a][b] = i
            #     b = b + 1

            # image = list(map(list, result))
            # for a in range(img.height):
            #     for b in range(img.width):
            #         x = int(result[a][b])
            image = [['' for i in range(170)] for j in range(80)]
            for a in range(img.height):
                for b in range(img.width):
                    x = int(data[a][b][0])
                    # if x <= 3:
                    #     image[a][b] = str(" ")
                    # if 3 < x <= 24:
                    #     image[a][b] = str(".")
                    # if 24 < x <= 45:
                    #     image[a][b] = str(",")
                    # if 45 < x <= 66:
                    #     image[a][b] = str("-")
                    # if 66 < x <= 87:
                    #     image[a][b] = str("~")
                    # if 87 < x <= 108:
                    #     image[a][b] = str(":")
                    # if 108 < x <= 129:
                    #     image[a][b] = str(";")
                    # if 129 < x <= 150:
                    #     image[a][b] = str("=")
                    # if 150 < x <= 171:
                    #     image[a][b] = str("!")
                    # if 171 < x <= 192:
                    #     image[a][b] = str("*")
                    # if 192 < x <= 213:
                    #     image[a][b] = str("#")
                    # if 213 < x <= 234:
                    #     image[a][b] = str("$")
                    # if 234 < x <= 255:
                    #     image[a][b] = str("@")
                    if x <= 3:
                        image[a][b] = ' '
                    if 3 < x <= 24:
                        image[a][b] = '.'
                    if 24 < x <= 45:
                        image[a][b] = ','
                    if 45 < x <= 66:
                        image[a][b] = '-'
                    if 66 < x <= 87:
                        image[a][b] = '~'
                    if 87 < x <= 108:
                        image[a][b] = ':'
                    if 108 < x <= 129:
                        image[a][b] = ';'
                    if 129 < x <= 150:
                        image[a][b] = '='
                    if 150 < x <= 171:
                        image[a][b] = '!'
                    if 171 < x <= 192:
                        image[a][b] = '*'
                    if 192 < x <= 213:
                        image[a][b] = '#'
                    if 213 < x <= 234:
                        image[a][b] = '$'
                    if 234 < x <= 255:
                        image[a][b] = '@'

            line = ""
            # for x in range(img.height):
            #     for y in range(img.width):
            #         line = line + (image[x][y])
            #     self.__img_print[x] = line + "\n"
            #     # print(line)
            #     line = ""
            for x in range(img.height):
                self.__img_print[x] = line.join(image[x]) + "\n"
                line = ""
            self.fire()
            # sleep(0.2)

    def kill(self):
        self.__run = False
