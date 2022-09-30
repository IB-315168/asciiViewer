from kivy.app import App
from kivy.uix.widget import Widget


class AsciiViewer(Widget):
    pass


class AsciiViewerApp(App):
    def build(self):
        return AsciiViewer()


if __name__ == '__main__':
    AsciiViewerApp().run()