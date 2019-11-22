from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from playsom import PlaySom
from kivy.uix.screenmanager import ScreenManager, Screen


class Interface(ScreenManager):
    pass

class Tablet(Screen):
    def play_sample(self,keycode):
        play=PlaySom()
        play.play_samples(keycode)

class SelectSamples(Screen):
    pass

    
class SomPyApp(App):
    
    def build(self):
        Window.bind(on_key_down=self.on_keyboard_down)
        return Interface()

    def on_keyboard_down(self, window, keycode, *args):
        play=PlaySom()
        play.play_samples(keycode)
        
        
SomPyApp().run()
