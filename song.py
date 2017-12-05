import pygame

class Song:
    def __init__(self, filename,framesInEight, track1, track2, track3, track4):
        self.track1 = list(track1)
        self.track2 = list(track2)
        self.track3 = list(track3)
        self.track4 = list(track4)
        pygame.mixer.music.load(filename)

        self.framesInEight = framesInEight - 1
        self.spawnTimer = 0
        self.spawnIter = 0

    def playSong(self):
        pygame.mixer.music.play(0)

    def advFrame(self):
        output = {} #list length 4, a 1 reps a note, a 0 a rest, a 2 the end of the song

        if self.spawnTimer == self.framesInEight:
            self.spawnTimer = 0

            if(self.track1[self.spawnIter] == 2):
                output[1] = 2
            else:
                if(self.track1[self.spawnIter] == 1):
                    output[1] = 1
                else:
                    output[1] = 0
                if(self.track2[self.spawnIter] == 1):
                    output[2] = 1
                else:
                    output[2] = 0
                if(self.track3[self.spawnIter] == 1):
                    output[3] = 1
                else:
                    output[3] = 0
                if(self.track4[self.spawnIter] == 1):
                    output[4] = 1
                else:
                    output[4] = 0
                self.spawnIter += 1
                return output
        else:
            self.spawnTimer += 1
        return {}
