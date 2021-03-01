
from kivy.uix.screenmanager import Screen
from keyboard import Keyboard


class Home(Screen):
    def __init__(self):
        super(Home, self).__init__()
        self.name='Home'


keyboard = Keyboard().setKeyboard()
home = Home()
home.add_widget(keyboard)
