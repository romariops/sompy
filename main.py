from kivy.app import App
from kivy.core.window import Window
from playsound import PlaySom
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

from select_sample import SelectSamples
from button_custom import ButtonCustom

Builder.load_file('inicial_screen.kv')
Builder.load_file('select_samples_screen.kv')


class Interface(ScreenManager):
    pass


class Tablet(Screen):
    pass


class SomPyApp(App):
    
    def build(self):
        Window.bind(on_key_down=self.on_keyboard_down)
        return Interface()

    def on_keyboard_down(self, window, keycode, *args):
        play = PlaySom()
        if keycode in play.keycodes.keys():
            play.fix_functions_in_keycodes()
            play.keycodes[keycode](keycode)


SomPyApp().run()
