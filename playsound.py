
import pygame
pygame.mixer.init()


class PlaySom:
    
    def __init__(self):
        self.keycodes = {
            49: None, 50: None, 51: None, 52: None, 53: None, 54: None, 55: None, 56: None, 57: None, 48: None,
            113: None, 119: None, 101: None, 114: None, 116: None, 121: None, 117: None, 105: None, 111: None, 112: None,
            97: None, 115: None, 100: None, 102: None, 103: None, 104: None, 106: None, 107: None, 108: None, 231: None,
            122: None, 120: None, 99: None, 118: None, 98: None, 110: None, 109: None, 44: None, 46: None, 56: None
        }

        self.sourcs_samples = {
            49:"sounds/BD-ER01.wav",
            50:"sounds/BD-ER02.wav",
            51:"sounds/BD-ER03.wav",
            52:"sounds/BD-ER04.wav",
            53:"sounds/BD-ER05.wav",
            54:"sounds/BD-ER06.wav",
            55:"sounds/BD-ER07.wav",
            56:"sounds/BD-ER08.wav",
            57:"sounds/BD-ER09.wav",
            48:"sounds/BD-ER10.wav",

            113: "sounds/BD-ER11.wav",
            119: "sounds/BD-ER12.wav",
            101: "sounds/BD-ER13.wav",
            114: "sounds/BD-ER14.wav",
            116: "sounds/BD-ER15.wav",
            121: "sounds/BD-ER16.wav",
            117: "sounds/BD-ER17.wav",
            105: "sounds/BD-ER18.wav",
            111: "sounds/BD-ER19.wav",
            112: "sounds/BD-ER20.wav",

            97: "sounds/BD-ER21.wav",
            115: "sounds/BD-ER22.wav",
            100: "sounds/BD-ER23.wav",
            102: "sounds/BD-ER24.wav",
            103: "sounds/BD-ER25.wav",
            104: "sounds/BD-ER26.wav",
            106: "sounds/BD-ER27.wav",
            107: "sounds/BD-ER28.wav",
            108: "sounds/BD-ER29.wav",
            231: "sounds/BD-ER30.wav",

            122: "sounds/BD-ER31.wav",
            120: "sounds/BD-ER32.wav",
            99: "sounds/BD-ER33.wav",
            118: "sounds/BD-ER34.wav",
            98: "sounds/BD-ER35.wav",
            110: "sounds/BD-ER36.wav",
            109: "sounds/BD-ER37.wav",
            44: "sounds/BD-ER38.wav",
            46: "sounds/BD-ER39.wav",
            56: "sounds/BD-ER40.wav"
        }

    def play_samples(self, keycode):
        pygame.mixer.music.load(self.sourcs_samples[keycode])
        pygame.mixer.music.play()

    def fix_functions_in_keycodes(self):
        for key in self.keycodes.keys():
            self.keycodes[key] = self.play_samples

    

