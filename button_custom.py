from kivy.uix.button import Button


class ButtonCustom(Button):
    def __init__(self, **kwargs):
        super(ButtonCustom, self).__init__(**kwargs)
        self.keycode = None
        self.matrix_index_i = None
        self.matrix_index_j = None
        self.loop = False
        self.bold = True