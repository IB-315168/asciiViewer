import pyautogui
import pyscreenshot as pyscreenshot

from pynput import mouse
from kivy.properties import StringProperty
from kivy.uix.widget import Widget

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
        if not self.screen_scan:
            ScreenCap.listener.start()
            self.screen_scan = True
        else:
            ScreenCap.listener.stop()
            self.screen_scan = False
        while not ScreenCap.ScreenCap.complete:
            self.random_number = "<{x1},{y1},{x2},{y2}>".format(x1=ScreenCap.ScreenCap.xPos1, y1=ScreenCap.ScreenCap.yPos1,
                                                                x2=ScreenCap.ScreenCap.xPos2, y2=ScreenCap.ScreenCap.yPos2)
        self.screenShot()

    def screenShot(self):
        im = pyscreenshot.grab(bbox=(ScreenCap.ScreenCap.xPos1, ScreenCap.ScreenCap.yPos1,
                                     ScreenCap.ScreenCap.xPos2, ScreenCap.ScreenCap.yPos2))
        im.show()