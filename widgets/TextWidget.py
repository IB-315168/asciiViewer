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
    captureThread: threading.Thread

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.__listeners = []
        self.random_number = "0000000000000000000000000000000000000000000000000000" \
                             + "0000000000000000000000000000000000000000000000000000000000000000000000 "

    def change_text(self):
        listener = mouse.Listener(
            on_click=ScreenCap.on_click)
        listener.start()
        ScreenCap.ScreenCap.complete = False

        while not ScreenCap.ScreenCap.complete:
            self.random_number = "<{x1},{y1},{x2},{y2}>".format(x1=ScreenCap.ScreenCap.pos[0], y1=ScreenCap.ScreenCap.pos[1],
                                                                x2=ScreenCap.ScreenCap.pos[2], y2=ScreenCap.ScreenCap.pos[3])
        self.a_v.setBBox(ScreenCap.ScreenCap.pos)
        listener.stop()

    def startCapture(self):
        self.a_v.add_listener(self.setLabel)
        self.captureThread = threading.Thread(target=self.a_v.screencap)
        self.captureThread.start()

            # im = pyscreenshot.grab(bbox=(ScreenCap.ScreenCap.xPos1, ScreenCap.ScreenCap.yPos1,
        #                              ScreenCap.ScreenCap.xPos2, ScreenCap.ScreenCap.yPos2))
        # im.show()
    def setLabel(self, imgprint):
        self.random_number = ""
        for i in range(80):
            self.random_number += imgprint[i]

    def stopCapture(self):
        if self.captureThread.is_alive():
            self.a_v.kill()
            self.a_v.remove_listener(self.setLabel)



