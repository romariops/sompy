
from keyboard import Keyboard
from play import Play


class Manager:
    def __init__(self):
        self.play = Play()

    def control(self, keycode):

        for button in Keyboard().keys_keyboard_play_samples:
            if button.keycode == keycode:
                self.play.play_sample(keycode)

