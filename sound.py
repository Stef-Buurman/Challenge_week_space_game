import sys
from threading import Timer
sys.path.append('Libraries\pygame')
import pygame

class Sound:
    def __init__(self, sound, soundTime, background = False):
        self.sound = sound
        self.soundTime = soundTime
        self.background = background
    
    def play(self):
        pygame.mixer.init()
        self.soundPlayer = pygame.mixer.Sound(self.sound)
        self.soundPlayer.play()
        if self.background and self.soundTime > 0:
            Timer(self.soundTime, self.soundPlayer.stop()).start()
    
    def stop(self):
        self.soundPlayer.stop()