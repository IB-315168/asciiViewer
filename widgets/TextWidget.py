import random
from kivy.properties import StringProperty
from kivy.uix.widget import Widget


class TextWidget(Widget):
    random_number = StringProperty()

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.random_number = str(random.randint(1, 100))

    def change_text(self):
        self.random_number = str(random.randint(1, 100))
