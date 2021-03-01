
from kivy.uix.button import Button
from play import Play


class ButtonKeyboardPlaySamples(Button):
    def __init__(self,  **kwargs,):
        super(ButtonKeyboardPlaySamples, self).__init__()
        self._keycode = kwargs['keycode']
        self._matrix_index_i = kwargs['matrix_index_line']
        self._matrix_index_j = kwargs['matrix_index_column']
        self._loop = False
        self.bold = True
        self._source_of_sample = ''
        self.text = kwargs['text']
        self.play = Play()

    @property
    def loop(self):
        return self._loop

    @loop.setter
    def loop(self, loop):
        self._loop = loop

    @property
    def source_of_sample(self):
        return self._source_of_sample

    @property
    def keycode(self):
        return self._keycode

    def on_press(self):
        self.play.play_sample(self.keycode)



