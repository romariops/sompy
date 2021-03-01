
from kivy.uix.button import Button


class ButtonMenuUp(Button):
    def __init__(self, **kwargs):
        super(ButtonMenuUp, self).__init__(**kwargs)
        self.bold = True
