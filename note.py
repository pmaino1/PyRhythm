import pygame

class Note(pygame.sprite.Sprite):
    def __init__(self,image, x, y, speed, trackhit = 0):

        pygame.sprite.Sprite.__init__(self)

        self.image =  pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.speed = speed

        self.ogImage = self.image            #ONLY FOR THE CATCHERS AS WELL
        self.trackhit = trackhit             #ONLY FOR THE CATCHERS, CONTROLLS WHEN TO CHANGE THE CATCHER TO GREY

    def move(self):
        self.rect.y += self.speed
