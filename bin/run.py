import pygame
from random import randint
from gracz import all_sprites_list, SpriteGenerator, all_bombs_list
#Autor: Jan Maciuk

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SKYBLUE = (135, 206, 235)

pygame.init()
pygame.display.set_caption("Super Gra!")
screen_height = 720
screen_width = 1280
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_icon(pygame.transform.scale(pygame.image.load("ikona-programu.gif").convert_alpha(),(32,32)))

playerSprite = SpriteGenerator(1,135,70)
playerSprite.rect.x = (screen_width/2 - 75)
playerSprite.rect.y = 650
screen_rect = pygame.Rect((0, 0), (1280, 720))

clock = pygame.time.Clock()
mainloop = True
playtime = 0
playerSpeed = 8

while mainloop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False
                
    playerSprite.rect.clamp_ip(screen_rect)
    collision_list = pygame.sprite.spritecollide(playerSprite,all_bombs_list,False)
    for bomb in collision_list:
        print("wykryto kolizje!")
        mainloop = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerSprite.moveLeft(playerSpeed)
    if keys[pygame.K_RIGHT]:
        playerSprite.moveRight(playerSpeed)

    if(randint(1,20) == 10):
        SpriteGenerator(2,150,419)
        
    
    for x in all_sprites_list:
        x.moveForward()

    milliseconds = clock.tick(60) 
    playtime += milliseconds / 1000.0
    all_sprites_list.update()

    pygame.display.set_caption("Czas gry: " + str(round(playtime,1)) + " sekund")

    screen.fill(SKYBLUE)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    

print("Autor: Jan Maciuk")
pygame.quit()