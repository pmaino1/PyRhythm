import pygame

class Song:
    def __init__(self, filename,framesInEight, track1, track2, track3, track4):
        """
        Creates list for each track, loads the song, and tracks the frames in each eighth note.
        param:(object,file,int,list) needs self, song file, the amount of frames in an eighth note, list of tracks
        return (None)
        """
        self.track1 = list(track1)
        self.track2 = list(track2)
        self.track3 = list(track3)
        self.track4 = list(track4)
        pygame.mixer.music.load(filename)

        self.framesInEight = framesInEight - 1
        self.spawnTimer = 0
        self.spawnIter = 0

    def playSong(self):
        """
        Plays the song file.
        param:(object) only needs self
        return (None)
        """
        pygame.mixer.music.play(0)

    def advFrame(self):
        """
        Runs through the amount of frames per eighth note and spawns notes on each track.
        param:(object) only needs self
        return {}
        """
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
