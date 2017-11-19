import pygame

class Note(pygame.sprite.Sprite):
    def __init__(self,image, x, y, speed):

        pygame.sprite.Sprite.__init__(self)

        self.image =  pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.speed = speed


    def move(self):
        self.rect.y += self.speed
