import threading

from pynput import mouse
from kivy.properties import StringProperty
from kivy.uix.widget import Widget

import legacy.asciiView as asciiView
from logic import ScreenCap


class TextWidget(Widget):
    random_number = StringProperty()
    a_v = asciiView.AsciiView()
    screen_scan = False

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.__listeners = []

        self.random_number = "0000000000000000000000000000000000000000000000000000" \
                             + "0000000000000000000000000000000000000000000000000000000000000000000000 "

    def change_text(self):
        listener = mouse.Listener(
            on_move=ScreenCap.on_move,
            on_click=ScreenCap.on_click,
            on_scroll=ScreenCap.on_scroll)
        listener.start()
        ScreenCap.ScreenCap.complete = False

        while not ScreenCap.ScreenCap.complete:
            self.random_number = "<{x1},{y1},{x2},{y2}>".format(x1=ScreenCap.ScreenCap.xPos1, y1=ScreenCap.ScreenCap.yPos1,
                                                                x2=ScreenCap.ScreenCap.xPos2, y2=ScreenCap.ScreenCap.yPos2)
        listener.stop()

    def screenShot(self):
        self.a_v.add_listener(self.setLabel)
        x = threading.Thread(target=self.a_v.screencap, args=(ScreenCap.ScreenCap.xPos1, ScreenCap.ScreenCap.yPos1,
                                                              ScreenCap.ScreenCap.xPos2, ScreenCap.ScreenCap.yPos2))
        x.start()

            # im = pyscreenshot.grab(bbox=(ScreenCap.ScreenCap.xPos1, ScreenCap.ScreenCap.yPos1,
        #                              ScreenCap.ScreenCap.xPos2, ScreenCap.ScreenCap.yPos2))
        # im.show()
    def setLabel(self, imgprint):
        self.random_number = ""
        for i in range(80):
            self.random_number += imgprint[i]


