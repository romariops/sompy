from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.screenmanager import Screen
import os


class FileChoo(FileChooserIconView):
    def on_selection(self, *args):
        print(self.selection)


class SelectSamples(Screen):

    def select_sample(self):

        box = BoxLayout()
        filechoo = FileChoo()
        box.add_widget(filechoo)

        popup = Popup(
            title='SomPy',
            content=box,
            size_hint=(None, None),
            size=(700, 500),
            auto_dismiss=True
        )
        popup.open()
