import pygame

class Note(pygame.sprite.Sprite):
    def __init__(self,image, x, y, speed, trackhit = 0):
        """
        Creates the notes that appear on screen.
        param:(object,image,int,int,int,int) needs self, a note image, position,speed,collision)
        return (None)
        """

        pygame.sprite.Sprite.__init__(self)

        self.image =  pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.speed = speed

        self.ogImage = self.image            #ONLY FOR THE CATCHERS AS WELL
        self.trackhit = trackhit             #ONLY FOR THE CATCHERS, CONTROLS WHEN TO CHANGE THE CATCHER TO GREY

    def move(self):
        """
        Moves the note by changing its vertical position.
        param:(object) only needs self
        return (None)
        """
        self.rect.y += self.speed
