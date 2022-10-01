import random

from kivy.app import App
from kivy.config import Config
from kivy.properties import StringProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget

Config.set('graphics', 'resizable', False)


class AsciiViewer(RelativeLayout):
    pass


class TextWidget(Widget):
    random_number = StringProperty()

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.random_number = str(random.randint(1, 100))

    def change_text(self):
        self.random_number = str(random.randint(1, 100))


class AsciiViewerApp(App):
    def build(self):
        return AsciiViewer()


if __name__ == '__main__':
    AsciiViewerApp().run()
