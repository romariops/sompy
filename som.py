import pygame

from pygame.locals import *
pygame.init()

class PlaySom:
    
    def __init__(self):
        pass

    def play_samples(self, keycode):
        
        if keycode == 49:
            self.code49(keycode)


        if keycode == 50:
            self.code50(keycode)

        if keycode == 51:
            self.code51(keycode)

        if keycode == 52:
            self.code52(keycode)

        if keycode == 53:
            self.code53(keycode)

        if keycode == 54:
            self.code54(keycode)

        if keycode == 55:
            self.code55(keycode)

        if keycode == 56:
            self.code56(keycode)

        if keycode == 57:
            self.code57(keycode)
            
        if keycode == 48:
            self.code48(keycode)

        if keycode == 45:
            self.code45(keycode)
        
        if keycode == 61:
            self.code61(keycode)

        if keycode == 113:
            self.code113(keycode)

        if keycode == 119:
            self.code119(keycode)

        if keycode == 101:
            self.code101(keycode)

        if keycode == 114:
            self.code114(keycode)

        if keycode == 116:
            self.code116(keycode)

        if keycode == 121:
            self.code121(keycode)

        if keycode == 117:
            self.code117(keycode)

        if keycode == 105:
            self.code105(keycode)
            
        if keycode == 111:
            self.code111(keycode)
            
        if keycode == 112:
            self.code112(keycode)
        
        if keycode == 1073741824:
            self.code1073741824(keycode)

        if keycode == 91:
            self.code91(keycode)

        if keycode == 97:
            self.code97(keycode)

        if keycode == 115:
            self.code115(keycode)

        if keycode == 100:
            self.code100(keycode)

        if keycode == 102:
            self.code102(keycode)

        if keycode == 103:
            self.code103(keycode)

        if keycode == 104:
            self.code104(keycode)

        if keycode == 106:
            self.code106(keycode)
            
        if keycode == 107:
            self.code107(keycode)
            
        if keycode == 108:
            self.code108(keycode)
        
        if keycode == 231:
            self.code231(keycode)

        if keycode == 1073741824:
            self.code1073741824(keycode)

        if keycode == 93:
            self.code93(keycode)

        if keycode == 92:
            self.code92(keycode)

        if keycode == 122:
            self.code122(keycode)

        if keycode == 120:
            self.code120(keycode)

        if keycode == 99:
            self.code99(keycode)

        if keycode == 118:
            self.code118(keycode)

        if keycode == 98:
            self.code98(keycode)
            
        if keycode == 110:
            self.code110(keycode)
            
        if keycode == 109:
            self.code109(keycode)
        
        if keycode == 44:
            self.code44(keycode)
            
        if keycode == 46:
            self.code46(keycode)
            
        if keycode == 59:
            self.code59(keycode)
        
        if keycode == 47:
            self.code47(keycode)
        

    def code49(self,keyborad):
        sample = pygame.mixer.Sound('samples/Avicii_Levels_Skrillex_Remix/01.wav')
        sample.play()
    
    def code50(self,keyborad):
        sample = pygame.mixer.Sound('samples/Avicii_Levels_Skrillex_Remix/02.wav')
        sample.play()

    def code51(self,keyborad):
        sample = pygame.mixer.Sound('samples/Avicii_Levels_Skrillex_Remix/03.wav')
        sample.play()
    
    def code52(self,keyborad):
        sample = pygame.mixer.Sound('samples/Avicii_Levels_Skrillex_Remix/04.wav')
        sample.play()
    
    def code53(self,keyborad):
        sample = pygame.mixer.Sound('samples/Avicii_Levels_Skrillex_Remix/05.wav')
        sample.play()
    
    def code54(self,keyborad):
        sample = pygame.mixer.Sound('samples/Avicii_Levels_Skrillex_Remix/06.wav')
        sample.play()

    def code55(self,keyborad):
        sample = pygame.mixer.Sound('samples/Avicii_Levels_Skrillex_Remix/07.wav')
        sample.play()
    
    def code56(self,keyborad):
        sample = pygame.mixer.Sound('samples/Avicii_Levels_Skrillex_Remix/08.wav')
        sample.play()
    
    def code57(self,keyborad):
        sample = pygame.mixer.Sound('samples/Avicii_Levels_Skrillex_Remix/09.wav')
        sample.play()
    
    def code48(self,keyborad):
        sample = pygame.mixer.Sound('samples/Avicii_Levels_Skrillex_Remix/10.wav')
        sample.play()

    def code45(self,keyborad):
        sample = pygame.mixer.Sound('samples/Avicii_Levels_Skrillex_Remix/11.wav')
        sample.play()
    
    def code61(self,keyborad):
        sample = pygame.mixer.Sound('samples/Avicii_Levels_Skrillex_Remix/12.wav')
        sample.play()
    
    def code113(self,keyborad):
        sample = pygame.mixer.Sound('samples/Avicii_Levels_Skrillex_Remix/13.wav')
        sample.play()
    
    def code119(self,keyborad):
        sample = pygame.mixer.Sound('samples/Avicii_Levels_Skrillex_Remix/14.wav')
        sample.play()

    def code101(self,keyborad):
        sample = pygame.mixer.Sound('samples/Avicii_Levels_Skrillex_Remix/15.wav')
        sample.play()
    
    def code114(self,keyborad):
        sample = pygame.mixer.Sound('samples/Avicii_Levels_Skrillex_Remix/16.wav')
        sample.play()

    def code116(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Bangarang/01.wav')
        sample.play()
    
    def code121(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Bangarang/02.wav')
        sample.play()

    def code117(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Bangarang/03.wav')
        sample.play()
    
    def code105(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Bangarang/04.wav')
        sample.play()
    
    def code111(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Bangarang/05.wav')
        sample.play()
    
    def code112(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Bangarang/06.wav')
        sample.play()

    def code1073741824(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Bangarang/07.wav')
        sample.play()
    
    def code91(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Bangarang/08.wav')
        sample.play()
    
    def code97(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Bangarang/09.wav')
        sample.play()
    
    def code115(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Bangarang/10.wav')
        sample.play()

    def code100(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Bangarang/11.wav')
        sample.play()
    
    def code102(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Bangarang/12.wav')
        sample.play()
    
    def code103(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Bangarang/13.wav')
        sample.play()
    
    def code104(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Bangarang/14.wav')
        sample.play()

    def code106(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Bangarang/15.wav')
        sample.play()
    
    def code107(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Bangarang/16.wav')
        sample.play()

    def code108(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Cinema/01.wav')
        sample.play()
    
    def code231(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Cinema/02.wav')
        sample.play()

    def code1073741824(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Cinema/03.wav')
        sample.play()
    
    def code93(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Cinema/04.wav')
        sample.play()
    
    def code92(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Cinema/05.wav')
        sample.play()
    
    def code122(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Cinema/06.wav')
        sample.play()

    def code120(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Cinema/07.wav')
        sample.play()
    
    def code99(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Cinema/08.wav')
        sample.play()
    
    def code118(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Cinema/09.wav')
        sample.play()
    
    def code98(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Cinema/10.wav')
        sample.play()
    
    def code110(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Cinema/11.wav')
        sample.play()
    
    def code109(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Cinema/12.wav')
        sample.play()
    
    def code44(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Cinema/13.wav')
        sample.play()
    
    def code46(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Cinema/14.wav')
        sample.play()
    
    def code59(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Cinema/15.wav')
        sample.play()
    
    def code47(self,keyborad):
        sample = pygame.mixer.Sound('samples/Skrillex_Cinema/16.wav')
        sample.play()
    

