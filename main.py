from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from som import PlaySom

class Tablet(BoxLayout):
    def __init__(self):
        super().__init__()
    
    def play_sample(self,keycode):
        play=PlaySom()
        play.play_samples(keycode)

    
class SomPyApp(App):
    
    def build(self):
        Window.bind(on_key_up=self.on_keyboard_up)
        return Tablet()

    def on_keyboard_up(self, window, keycode, *args):
        play=PlaySom()
        play.play_samples(keycode)
        
        
SomPyApp().run()
