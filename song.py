import pygame

class Song:
    def __init__(self, filename, track1, track2, track3, track4):
        self.track1 = list(track1)
        self.track2 = list(track2)
        self.track3 = list(track3)
        self.track4 = list(track4)
        pygame.mixer.music.load(filename)

    def playSong(self):
        pygame.mixer.music.play(0)
