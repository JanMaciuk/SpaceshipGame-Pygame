import pygame
from random import randint
from threading import Timer
#Autor: Jan Maciuk

all_sprites_list = pygame.sprite.Group()
all_bombs_list = pygame.sprite.Group()
WHITE = (255, 255, 255)
BLACK = ( 0, 0, 0)

class SpriteGenerator(pygame.sprite.Sprite):
    
    def __init__(self, type, width, height):
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        def destructor():
            all_sprites_list.remove(self)
            all_bombs_list.remove(self)

        if type == 1:
            self.image = pygame.image.load("sprite-ufo.png").convert_alpha()
            self.bombSpeed = 0
        elif type == 2:
            self.image = pygame.image.load("sprite-bomb.png").convert_alpha()
            self.bombSpeed = randint(3,6)
            t = Timer(4.0,destructor)
            t.start()
        
        self.rect = self.image.get_rect()
        self.rect.y = 1
        self.rect.x = randint(1,1230)
        if type == 2: all_bombs_list.add(self)
        all_sprites_list.add(self)
    
    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels
    
    def moveForward(self):
        self.rect.y += self.bombSpeed