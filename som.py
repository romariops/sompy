
import pygame
import os

pygame.init()

class PlaySom():
    def __init__(self):
        self.sounds_names={113:"01.wav",119:"02.wav",101:"03.wav",114:"04.wav",
            116:"05.wav",121:"06.wav",117:"07.wav",105:"08.wav",111:"09.wav",112:"10.wav",
            1073741824:"11.wav",91:"12.wav",97:"13.wav",115:"14.wav",100:"15.wav",102:"16.wav"}

    def play(self,keycode):
        
        if os.path.exists('samples/Avicii_Levels_Skrillex_Remix/'+self.sounds_names[keycode]):
            pygame.mixer.music.load('samples/Avicii_Levels_Skrillex_Remix/'+self.sounds_names[keycode])
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.event.poll()
        else:
            print('O arquivo musica.mp3 não está no diretório do script Python')


