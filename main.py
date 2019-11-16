from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader


class Tablet(BoxLayout):
    pass

    
class SomPyApp(App):
    def build(self):
        Window.bind(on_key_down=self.on_keyboard_down)
        return Tablet()

    def on_keyboard_down(self, window, keycode, *args):
        print(keycode)
        

SomPyApp().run()
