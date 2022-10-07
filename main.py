from widgets import TextWidget
from kivy.app import App
from kivy.config import Config
from kivy.uix.relativelayout import RelativeLayout

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '1030')
Config.set('graphics', 'height', '900')


class AsciiViewer(RelativeLayout):
    pass


class AsciiViewerApp(App):
    def build(self):
        return AsciiViewer()


if __name__ == '__main__':
    AsciiViewerApp().run()
