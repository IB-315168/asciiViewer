import threading

import pyautogui
import pyscreenshot as pyscreenshot

from pynput import mouse
from kivy.properties import StringProperty
from kivy.uix.widget import Widget

import legacy.asciiView as asciiView
from logic import ScreenCap


def selectArea():
    return pyautogui.position()


class TextWidget(Widget):
    random_number = StringProperty()
    screen_scan = False

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)

        self.random_number = "0000000000000000000000000000000000000000000000000000" \
                             + "0000000000000000000000000000000000000000000000000000000000000000000000 "

    def change_text(self):
        listener = mouse.Listener(
            on_move=ScreenCap.on_move,
            on_click=ScreenCap.on_click,
            on_scroll=ScreenCap.on_scroll)
        listener.start()
        ScreenCap.ScreenCap.complete = False

        # if not self.screen_scan:
        #     ScreenCap.listener.start()
        #     self.screen_scan = True
        # else:
        #     ScreenCap.listener.stop()
        #     self.screen_scan = False
        while not ScreenCap.ScreenCap.complete:
            self.random_number = "<{x1},{y1},{x2},{y2}>".format(x1=ScreenCap.ScreenCap.xPos1, y1=ScreenCap.ScreenCap.yPos1,
                                                                x2=ScreenCap.ScreenCap.xPos2, y2=ScreenCap.ScreenCap.yPos2)
        listener.stop()
        # self.screenShot()

    def screenShot(self):
        event = threading.Event()
        x = threading.Thread(target=asciiView.screencap, args=(event, ScreenCap.ScreenCap.xPos1,
                                                                      ScreenCap.ScreenCap.yPos1,
                                   ScreenCap.ScreenCap.xPos2, ScreenCap.ScreenCap.yPos2))
        x.start()

        y = threading.Thread(target=self.setLabel, args=(event))
        y.start()

            # im = pyscreenshot.grab(bbox=(ScreenCap.ScreenCap.xPos1, ScreenCap.ScreenCap.yPos1,
        #                              ScreenCap.ScreenCap.xPos2, ScreenCap.ScreenCap.yPos2))
        # im.show()
    def setLabel(self, event):
        while True:
            event.wait()
            self.random_number = ""
            img = asciiView.img_print
            for i in range(80):
                self.random_number += img[i]


