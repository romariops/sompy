
from kivy.uix.button import Button


class ButtonMenuRight(Button):
    def __init__(self, **kwargs):
        super(ButtonMenuRight, self).__init__(**kwargs)
        self.bold = True