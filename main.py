import pygame #imports the basic pygame modules, pygame has many other modules inside of it as well, this will import most of them
import note
import song
import songInfo1

class Controller:
    def __init__(self, width =640, height = 480):
            pygame.init()#initialized most of the pygame modules, you need to do this or stuff wont work
            self.width = width
            self.height = height
            self.screen = pygame.display.set_mode((self.width, self.height))  #sets up a display object
            pygame.display.set_caption("This is a caption")  #sets caption for window
            self.background = pygame.Surface(self.screen.get_size()).convert()

            self.gameClock = pygame.time.Clock()

            self.score = 0

            """
            THIS CODE IS A HOT PIECE OF GARBAGE IM SORRY TEXT ME IF YOU DONT GET IT
            IM SETTING ALL THE BPM AS 1 FOR NOW, WILL NEED TO MAKE VARIABLE EVENTUALLY
            SO DONT FORGET THAT
            """

            self.testSong = song.Song(1, songInfo1.track1, songInfo1.track2, songInfo1.track3, songInfo1.track4)

            self.notes = []


            self.catcher1 = note.Note("assets/circle1.png",100, 400, 0)
            self.catcher2 = note.Note("assets/circle1.png",200, 400, 0)
            self.catcher3 = note.Note("assets/circle1.png",300, 400, 0)
            self.catcher4 = note.Note("assets/circle1.png",400, 400, 0)
            self.sprites = pygame.sprite.Group((self.notes,self.catcher1,self.catcher2,self.catcher3,self.catcher4))



    def mainLoop(self):
            spawnIter = 0   #iteration variable to control the song file reading
            crashed = False

            #### START OF GAME LOOP
            while not crashed:  #basic game loop, will run until we want to stop #most game logic will be here
                self.background.fill((255,255,255))
                self.gameClock.tick(30)
                ##EVENT LOOP
                for event in pygame.event.get():    #pygame has events: basically "when things happen"
                    if (event.type == pygame.QUIT):   #this will check if we do the quit event, and will crash the program
                        crashed = True
                    elif (event.type == pygame.KEYDOWN):    #key checker

                        if (event.key == pygame.K_q):   #checks to see if any notes are touching the catcher when q is pressed
                            for i in range(len(self.notes)):
                                #collisions\
                                if(pygame.sprite.collide_rect(self.notes[i], self.catcher1)):
                                    self.background.fill((250,0,0)) #if so do this
                                    self.score += 100
                        elif (event.key == pygame.K_w):
                            for i in range(len(self.notes)):
                                #collisions\
                                if(pygame.sprite.collide_rect(self.notes[i], self.catcher2)):
                                    self.background.fill((50,250,0))
                                    self.score += 100
                                    #add note deletion
                        elif (event.key == pygame.K_e):
                            for i in range(len(self.notes)):
                                #collisions\
                                if(pygame.sprite.collide_rect(self.notes[i], self.catcher3)):
                                    self.background.fill((50,0,0))
                                    self.score += 100
                                    #add note deletion
                        elif (event.key == pygame.K_r):
                            for i in range(len(self.notes)):
                                #collisions\
                                if(pygame.sprite.collide_rect(self.notes[i], self.catcher4)):
                                    self.background.fill((0,0,250))
                                    self.score += 100
                                    #add note deletion

                ##END OF EVENT LOOP

                #note spawning
                if(self.testSong.track1[spawnIter] == 2):
                    print("the end")
                else:
                    if(self.testSong.track1[spawnIter] == 1):
                        self.notes.append(note.Note("assets/circle1.png",100, 0, 1))
                    if(self.testSong.track2[spawnIter] == 1):
                        self.notes.append(note.Note("assets/circle1.png",200, 0, 1))
                    if(self.testSong.track3[spawnIter] == 1):
                        self.notes.append(note.Note("assets/circle1.png",300, 0, 1))
                    if(self.testSong.track4[spawnIter] == 1):
                        self.notes.append(note.Note("assets/circle1.png",400, 0, 1))
                    spawnIter += 1


                #moves all the notes
                for i in self.notes:
                    i.move()


                ###END OF GAME LOOP STUFF
                self.screen.blit(self.background, (0, 0))
                self.sprites = pygame.sprite.Group((self.notes,self.catcher1,self.catcher2,self.catcher3,self.catcher4))
                self.sprites.draw(self.screen)
                pygame.display.flip()
                #find way to delete excess notes

                #### END OF GAME LOOP




def main():
    program = Controller()
    program.mainLoop()
main()
