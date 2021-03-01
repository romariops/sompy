
from kivy.uix.screenmanager import ScreenManager
from launchPy_screens import home


class Interface(ScreenManager):
    def __init__(self):
        super(Interface, self).__init__()


interface = Interface()
interface.add_widget(home)

