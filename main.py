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
        Window.bind(on_key_down=self.on_keyboard_down)
        return Tablet()

    def on_keyboard_down(self, window, keycode, *args):
        play=PlaySom()
        play.play_samples(keycode)
        
        
SomPyApp().run()
