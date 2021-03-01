
from kivy.app import App
from launchPy_screenmanager import interface
from kivy.core.window import Window
from manager import Manager


class LaunchPyApp(App):

    def build(self):
        Window.bind(on_key_down=self.on_keyboard_down)
        return interface

    def on_keyboard_down(self, window, keycode, *args):
        Manager().control(keycode)


if __name__ == '__main__':
    LaunchPyApp().run()