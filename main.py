from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Tablet(BoxLayout):
    pass

class SomPyApp(App):
    def build(self):
        return Tablet()

SomPyApp().run()
