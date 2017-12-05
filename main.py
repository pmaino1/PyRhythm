import pygame, pygame.font #imports the basic pygame modules, pygame has many other modules inside of it as well, this will import most of them
import note
import song
import stacys_mom
import colorCycle
import random
import highscore

class Controller:
    def __init__(self, width =640, height = 480):
            pygame.init() #initialized most of the pygame modules, you need to do this or stuff wont work
            self.width = width
            self.height = height
            self.screen = pygame.display.set_mode((self.width, self.height))  #sets up a display object
            pygame.display.set_caption("PyRhythm!")  #sets caption for window
            self.background = pygame.Surface(self.screen.get_size()).convert()

            self.gameClock = pygame.time.Clock()    #clock object

            self.colorObj = colorCycle.ColorCycler()    #color object, reps the color of the background

            self.score = 0
            self.combo = 0
            self.highestCombo = 0
            self.highscoreObj = highscore.HighScore()   #score object that contains the scores from last plays

            #Text objects
            self.gameFont1 = pygame.font.SysFont("gadugi", 30)   #font object
            self.gameFont2 = pygame.font.SysFont("systembold", 60)
            self.controlText = self.gameFont1.render("Use Q, W, E, and R to hit the notes!", True, (255,255,255))
            self.startText = self.gameFont1.render("Press any key to start!", True, (255,255,255))
            self.titleText = self.gameFont2.render("PyRhythm!", True, (150, 200, 150))
            self.missText = self.gameFont1.render("Miss :(", True, (200,0,0))
            self.highscoreText = self.gameFont1.render(
            "High Score = " + str(self.highscoreObj.topScore) +
            ", High Combo = " + str(self.highscoreObj.topCombo),
            True, (0,150,0))

            self.missIter = 0   #variable that iterates to keep track of how long the miss animation is on screen for

            #Song Object
            self.Song1 = song.Song(stacys_mom.filename, stacys_mom.framesInEight, stacys_mom.track1, stacys_mom.track2, stacys_mom.track3, stacys_mom.track4)

            self.notes = []
            self.noteSpeed = 3
            self.noteclick = pygame.image.load("assets/noteclick.png")

            self.catcher1 = note.Note("assets/note1.png",150, 400, 0)
            self.catcher2 = note.Note("assets/note2.png",250, 400, 0)
            self.catcher3 = note.Note("assets/note3.png",350, 400, 0)
            self.catcher4 = note.Note("assets/note4.png",450, 400, 0)
            self.catchers = [self.catcher1, self.catcher2, self.catcher3, self.catcher4]

            self.sprites = pygame.sprite.Group((self.notes,self.catcher1,self.catcher2,self.catcher3,self.catcher4))


    def mainLoop(self):
            isSongStarted = False #var that keep track on whether the song has started or not
            isSongEnded = False

            ####TITLE SCREEN LOOP
            isTitleScreen = True
            while isTitleScreen:
                for event in pygame.event.get():
                    if (event.type == pygame.QUIT):   #this will check if we do the quit event, and will crash the program
                        isTitleScreen = False
                        crashed = True
                        break
                    if (event.type == pygame.KEYDOWN):  #will start the game if any key is pressed
                        isTitleScreen = False
                        break

                self.screen.blit(self.background, (0, 0))
                self.screen.blit(self.controlText, (50, 50))    #puts all the text on the screen
                self.screen.blit(self.startText, (50,90))
                self.screen.blit(self.titleText, (50,240))
                self.screen.blit(self.highscoreText, (50,380))
                pygame.display.flip()
            ####END OF TITLE SCREEN LOOP


            #### START OF GAME LOOP
            crashed = False
            while not crashed:  #basic game loop, will run until we want to stop #most game logic will be here

                #Makes background cycle between colors
                self.colorObj.cycle(self.background)

                self.gameClock.tick_busy_loop(40)
                print(self.gameClock.get_fps())
                ##EVENT LOOP
                for event in pygame.event.get():    #pygame has events: basically "when things happen"
                    if (event.type == pygame.QUIT):   #this will check if we do the quit event, and will crash the program
                        crashed = True
                    elif (event.type == pygame.KEYDOWN):    #key checker

                        if (event.key == pygame.K_q):   #checks to see if any notes are touching the catcher when q is pressed
                            self.catcher1.trackhit = 5     #tells the controller below to change the catcher's color
                            for i in range(len(self.notes)):
                                #collisions\
                                if(pygame.sprite.collide_rect(self.notes[i], self.catcher1)):
                                    self.score += 100
                                    self.combo += 1
                                    self.notes[i].kill()    #adds to score and delete the note
                                    del self.notes[i]
                                    break
                                if self.score >= 50:             #if no note is colliding with the catcher, you are penalized
                                    self.score -= 50
                                    self.missIter = 6
                                else:
                                    self.score = 0
                                    self.missIter = 6

                        elif (event.key == pygame.K_w):
                            self.catcher2.trackhit = 5     #tells the controller below to change the catcher's color
                            for i in range(len(self.notes)):
                                #collisions\
                                if(pygame.sprite.collide_rect(self.notes[i], self.catcher2)):
                                    self.score += 100
                                    self.combo += 1
                                    self.notes[i].kill()
                                    del self.notes[i]
                                    break
                                if self.score >= 50:
                                    self.score -= 50
                                    self.missIter = 6
                                else:
                                    self.score = 0
                                    self.missIter = 6

                        elif (event.key == pygame.K_e):
                            self.catcher3.trackhit = 5     #tells the controller below to change the catcher's color
                            for i in range(len(self.notes)):
                                #collisions\
                                if(pygame.sprite.collide_rect(self.notes[i], self.catcher3)):
                                    self.score += 100
                                    self.combo += 1
                                    self.notes[i].kill()
                                    del self.notes[i]
                                    break
                                if self.score >= 50:
                                    self.score -= 50
                                    self.missIter = 6
                                else:
                                    self.score = 0
                                    self.missIter = 6

                        elif (event.key == pygame.K_r):
                            self.catcher4.trackhit = 5     #tells the controller below to change the catcher's color
                            for i in range(len(self.notes)):
                                #collisions\
                                if(pygame.sprite.collide_rect(self.notes[i], self.catcher4)):
                                    self.score += 100
                                    self.combo += 1
                                    self.notes[i].kill()
                                    del self.notes[i]
                                    break
                                if self.score >= 50:
                                    self.score -= 50
                                    self.missIter = 6
                                else:
                                    self.score = 0
                                    self.missIter = 6


                ##END OF EVENT LOOP

                #Audio start controller
                """When the first note hits the catcher, isSongStarted becomes True, and the song begins."""
                if not isSongStarted:
                    for i in self.notes:
                        for j in self.catchers:
                            if pygame.sprite.collide_rect(i, j):
                                self.Song1.playSong()
                                isSongStarted = True
                                break
                        if isSongStarted:
                            break

                #CATCHER ANIMATION CONTROLLER
                """When a key is pressed the "trackhit" value for the catcher objects are set to 5,
                and when one of those values is non-0 this loop will change it to a "hit" ANIMATION
                 and will subtract 1 from trackhit, when trackhit is 0, it restores the catcher back to
                its original image (stored as ogImage)"""
                for i in self.catchers:
                    if i.trackhit == 1:
                        i.image = i.ogImage
                        i.trackhit -= 1
                    elif i.trackhit != 0:
                        i.image = self.noteclick
                        i.trackhit -= 1


                #note spawning
                """The notespawning system works as follows: For the song, which is 120 BPM, 10 ticks in 40 fps is an eighth note in the Song
                , so SpawnTimer will iterate 10 times. On the 10th iteration, it will increase another iteration variable, spawnIter, and then
                indexes the 4 lists of the song using spawnIter. Each list represents a track, and if it sees a 1 on that list, it will spawn a
                note on the corresponding track. 2 will signify the end of the program"""
                spawnDict = self.Song1.advFrame()   #spawnDict holds the 1, 0, or 2 from the track in the song class

                if spawnDict:   #if spawnDict isnt empty
                    if(spawnDict[1] == 2):
                        print('end')
                    else:
                        if(spawnDict[1] == 1):
                            self.notes.append(note.Note("assets/note1.png",150, 0, self.noteSpeed))
                        if(spawnDict[2] == 1):
                            self.notes.append(note.Note("assets/note2.png",250, 0, self.noteSpeed))
                        if(spawnDict[3] == 1):
                            self.notes.append(note.Note("assets/note3.png",350, 0, self.noteSpeed))
                        if(spawnDict[4] == 1):
                            self.notes.append(note.Note("assets/note4.png",450, 0, self.noteSpeed))


                #moves all the notes
                """ iterates through the list of note objects and calls their move method"""
                for i in self.notes:
                    i.move()


                #checks to see if notes have gone off the screen, if so delete them
                """ITerates through the list of notes, and deletes them if they have gone too low, as well well subtracting points from their score"""
                for i in range(len(self.notes)):
                    if(self.notes[i].rect.y > self.height - 50):
                        self.notes[i].kill()
                        del self.notes[i]
                        if self.score >= 50:
                            self.score -= 50
                        else:
                            self.score = 0
                        self.missIter += 5
                        break

                #if a miss happens, break the combo
                if self.missIter != 0:
                    self.combo = 0
                #keeps track of your highest combo
                if self.combo > self.highestCombo:
                    self.highestCombo = self.combo

                #HIGH SCORE HANDLING AT END OF SONG
                """IF there are no notes on the screen, and the song isnt ended, it will check if you beat the high highscores
                and will update them in the text file, then it will set the song as ended"""
                if not self.notes and not isSongEnded:  #if there are no notes on the screen
                    if self.score > self.highscoreObj.topScore:
                        self.highscoreObj.topScore = self.score
                    if self.highestCombo > self.highscoreObj.topCombo:
                        self.highscoreObj.topCombo = self.highestCombo
                    self.highscoreObj.export()
                    isSongEnded = True



                ###END OF GAME LOOP STUFF
                self.screen.blit(self.background, (0, 0))
                #updates the sprite group ( accounting for the deleted notes ) and displays it
                self.sprites = pygame.sprite.Group((self.notes,self.catcher1,self.catcher2,self.catcher3,self.catcher4))
                self.sprites.draw(self.screen)
                #updates score and displays it
                self.screen.blit(self.gameFont1.render("Score:"+str(self.score), True, (50,0,0)), (50,50))

                #Displays "Miss" is a note is missed
                """MissIter will be a non0 value if a note was missed, which will prompt this code block to displays
                the "Miss" test until MissIter returns to 0"""
                if(self.missIter > 0):
                    self.screen.blit(self.missText, (50+random.randrange(-10,10),75+random.randrange(-10,10)))
                    self.missIter -= 1
                #Only displays the combo is it is non 0
                if(self.combo != 0):
                    self.screen.blit(self.gameFont1.render(str(self.combo)+ "Hit!", True, (0,250,0)), (50,25))
                pygame.display.flip()

            #### END OF GAME LOOP




def main():
    program = Controller()
    program.mainLoop()
main()
