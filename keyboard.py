
from buttonKeyboardPlaySamples import ButtonKeyboardPlaySamples
from buttonMenuUp import ButtonMenuUp
from buttonMenuRight import ButtonMenuRight
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class Keyboard:

    def __init__(self):
        super(Keyboard, self).__init__()
        self.name = 'Keyboard'

        self._keys_menu_up = [
            ButtonMenuUp(text='F1'),
            ButtonMenuUp(text='F2'),
            ButtonMenuUp(text='F3'),
            ButtonMenuUp(text='F4'),
            ButtonMenuUp(text='F5'),
            ButtonMenuUp(text='F6'),
            ButtonMenuUp(text='F7'),
            ButtonMenuUp(text='F8'),
            ButtonMenuUp(text='F9'),
            ButtonMenuUp(text='F10'),
        ]

        self._keys_keyboard_play_samples = [
            ButtonKeyboardPlaySamples(text='1', keycode=49, matrix_index_line=0, matrix_index_column=0),
            ButtonKeyboardPlaySamples(text='2', keycode=50, matrix_index_line=0, matrix_index_column=1),
            ButtonKeyboardPlaySamples(text='3', keycode=51, matrix_index_line=0, matrix_index_column=2),
            ButtonKeyboardPlaySamples(text='4', keycode=52, matrix_index_line=0, matrix_index_column=3),
            ButtonKeyboardPlaySamples(text='5', keycode=53, matrix_index_line=0, matrix_index_column=4),
            ButtonKeyboardPlaySamples(text='6', keycode=54, matrix_index_line=0, matrix_index_column=5),
            ButtonKeyboardPlaySamples(text='7', keycode=55, matrix_index_line=0, matrix_index_column=6),
            ButtonKeyboardPlaySamples(text='8', keycode=56, matrix_index_line=0, matrix_index_column=7),
            ButtonKeyboardPlaySamples(text='9', keycode=57, matrix_index_line=0, matrix_index_column=8),
            ButtonKeyboardPlaySamples(text='0', keycode=48, matrix_index_line=0, matrix_index_column=9),

            ButtonKeyboardPlaySamples(text='Q', keycode=113, matrix_index_line=1, matrix_index_column=0),
            ButtonKeyboardPlaySamples(text='W', keycode=119, matrix_index_line=1, matrix_index_column=1),
            ButtonKeyboardPlaySamples(text='E', keycode=101, matrix_index_line=1, matrix_index_column=2),
            ButtonKeyboardPlaySamples(text='R', keycode=114, matrix_index_line=1, matrix_index_column=3),
            ButtonKeyboardPlaySamples(text='T', keycode=116, matrix_index_line=1, matrix_index_column=4),
            ButtonKeyboardPlaySamples(text='Y', keycode=121, matrix_index_line=1, matrix_index_column=5),
            ButtonKeyboardPlaySamples(text='U', keycode=117, matrix_index_line=1, matrix_index_column=6),
            ButtonKeyboardPlaySamples(text='I', keycode=105, matrix_index_line=1, matrix_index_column=7),
            ButtonKeyboardPlaySamples(text='O', keycode=111, matrix_index_line=1, matrix_index_column=8),
            ButtonKeyboardPlaySamples(text='P', keycode=112, matrix_index_line=1, matrix_index_column=9),

            ButtonKeyboardPlaySamples(text='A', keycode=97, matrix_index_line=2, matrix_index_column=0),
            ButtonKeyboardPlaySamples(text='S', keycode=115, matrix_index_line=2, matrix_index_column=1),
            ButtonKeyboardPlaySamples(text='D', keycode=100, matrix_index_line=2, matrix_index_column=2),
            ButtonKeyboardPlaySamples(text='F', keycode=102, matrix_index_line=2, matrix_index_column=3),
            ButtonKeyboardPlaySamples(text='G', keycode=103, matrix_index_line=2, matrix_index_column=4),
            ButtonKeyboardPlaySamples(text='H', keycode=104, matrix_index_line=2, matrix_index_column=5),
            ButtonKeyboardPlaySamples(text='J', keycode=106, matrix_index_line=2, matrix_index_column=6),
            ButtonKeyboardPlaySamples(text='K', keycode=107, matrix_index_line=2, matrix_index_column=7),
            ButtonKeyboardPlaySamples(text='L', keycode=108, matrix_index_line=2, matrix_index_column=8),
            ButtonKeyboardPlaySamples(text='Ç', keycode=231, matrix_index_line=2, matrix_index_column=9),

            ButtonKeyboardPlaySamples(text='Z', keycode=122, matrix_index_line=3, matrix_index_column=0),
            ButtonKeyboardPlaySamples(text='X', keycode=120, matrix_index_line=3, matrix_index_column=1),
            ButtonKeyboardPlaySamples(text='C', keycode=99, matrix_index_line=3, matrix_index_column=2),
            ButtonKeyboardPlaySamples(text='V', keycode=118, matrix_index_line=3, matrix_index_column=3),
            ButtonKeyboardPlaySamples(text='B', keycode=98, matrix_index_line=3, matrix_index_column=4),
            ButtonKeyboardPlaySamples(text='N', keycode=110, matrix_index_line=3, matrix_index_column=5),
            ButtonKeyboardPlaySamples(text='M', keycode=109, matrix_index_line=3, matrix_index_column=6),
            ButtonKeyboardPlaySamples(text=',', keycode=44, matrix_index_line=3, matrix_index_column=7),
            ButtonKeyboardPlaySamples(text='.', keycode=46, matrix_index_line=3, matrix_index_column=8),
            ButtonKeyboardPlaySamples(text=';', keycode=56, matrix_index_line=3, matrix_index_column=9),
        ]

        self._keys_menu_right = [
            ButtonMenuRight(text='Home'),
            ButtonMenuRight(text='PgUP'),
            ButtonMenuRight(text='PgDn'),
            ButtonMenuRight(text='End'),
        ]

    @property
    def keys_menu_up(self):
        return self._keys_menu_up

    @property
    def keys_keyboard_play_samples(self):
        return self._keys_keyboard_play_samples

    @property
    def keys_menu_right(self):
        return self._keys_menu_right

    def setLogo(self):

        box = BoxLayout(size_hint=(1, 0.10))
        logo = Label(text="LaunchPy", font_size=30, bold=True)
        box.add_widget(logo)

        return box

    def setKeyboardMenuUp(self):
        box = BoxLayout(orientation="horizontal", spacing=15, size_hint=(1, 0.15))

        for key in self.keys_menu_up:
            box.add_widget(key)

        return box

    def setKeyboarPlaySamples(self):

        box_line_1 = BoxLayout(spacing=5)
        for key in range(0, 9):
            box_line_1.add_widget(self.keys_keyboard_play_samples[key])

        box_line_2 = BoxLayout(spacing=5)
        for key in range(10, 19):
            box_line_2.add_widget(self.keys_keyboard_play_samples[key])

        box_line_3 = BoxLayout(spacing=5)
        for key in range(20, 29):
            box_line_3.add_widget(self.keys_keyboard_play_samples[key])

        box_line_4 = BoxLayout(spacing=5)
        for key in range(30, 39):
            box_line_4.add_widget(self.keys_keyboard_play_samples[key])

        box_keyboard_play_samples = BoxLayout(orientation="vertical", spacing=5)
        box_keyboard_play_samples.add_widget(box_line_1)
        box_keyboard_play_samples.add_widget(box_line_2)
        box_keyboard_play_samples.add_widget(box_line_3)
        box_keyboard_play_samples.add_widget(box_line_4)

        return box_keyboard_play_samples

    def setKeyboardMenuRight(self):

        box = BoxLayout(orientation="vertical", spacing=15,size_hint=(0.10, 1))

        for key in self.keys_menu_right:
            box.add_widget(key)

        return box

    def setKeyboard(self):

        box = BoxLayout(orientation="horizontal", spacing=5)
        box.add_widget(self.setKeyboarPlaySamples())
        box.add_widget(BoxLayout( size_hint=(0.01, 1)))
        box.add_widget(self.setKeyboardMenuRight())

        box_full_keyboard = BoxLayout(orientation='vertical', spacing=5, padding=10)
        box_full_keyboard.add_widget(self.setLogo())
        box_full_keyboard.add_widget(BoxLayout(size_hint=(1, 0.05)))
        box_full_keyboard.add_widget(self.setKeyboardMenuUp())
        box_full_keyboard.add_widget(BoxLayout(size_hint=(1, 0.05)))
        box_full_keyboard.add_widget(box)

        return box_full_keyboard


