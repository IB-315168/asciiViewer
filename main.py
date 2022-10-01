from widgets import TextWidget
from kivy.app import App
from kivy.config import Config
from kivy.uix.relativelayout import RelativeLayout

Config.set('graphics', 'resizable', False)


class AsciiViewer(RelativeLayout):
    pass


class AsciiViewerApp(App):
    def build(self):
        return AsciiViewer()


if __name__ == '__main__':
    AsciiViewerApp().run()
