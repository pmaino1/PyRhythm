import pygame #imports the basic pygame modules, pygame has many other modules inside of it as well, this will import most of them
import note

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

            self.testNote = note.Note("assets/circle.png",320, 100, 1)
            self.catcher = note.Note("assets/circle.png",320, 400, 0)
            self.sprites = pygame.sprite.Group((self.testNote,self.catcher))

    def mainLoop(self):
            crashed = False
            #### START OF GAME LOOP
            while not crashed:  #basic game loop, will run until we want to stop #most game logic will be here
                self.background.fill((250,250,250))
                self.gameClock.tick(30)
                ##EVENT LOOP
                for event in pygame.event.get():    #pygame has events: basically "when things happen"
                    if (event.type == pygame.QUIT):   #this will check if we do the quit event, and will crash the program
                        crashed = True              #if not, it prints out the type of event that was done
                    elif (event.type == pygame.KEYDOWN):
                        if (event.key == pygame.K_q):
                            #collisions
                            if(pygame.sprite.collide_rect(self.testNote, self.catcher)):
                                self.background.fill((250,0,0))
                ##END OF EVENT LOOP

                self.testNote.move()



                ###END OF GAME LOOP STUFF
                self.screen.blit(self.background, (0, 0))
                self.sprites.draw(self.screen)
                pygame.display.flip()
                #### END OF GAME LOOP




def main():
    program = Controller()
    program.mainLoop()
main()
