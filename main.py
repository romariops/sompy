from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from som import PlaySom

class Tablet(BoxLayout):
    pass
    
class SomPyApp(App):
    def build(self):
        Window.bind(on_key_up=self.on_keyboard_up)
        return Tablet()

    def on_keyboard_up(self, window, keycode, *args):
        print(keycode)
        play=PlaySom()
        play.play(keycode)
        
SomPyApp().run()
