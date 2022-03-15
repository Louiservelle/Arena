import pygame
from Player import Player
pygame.init()

pygame.display.set_caption("Arena")
size = 1080, 720
screen = pygame.display.set_mode(size)
background = pygame.image.load('asset-background2D/_PNG/1/background.png')
background = pygame.transform.scale(background, (1080, 720))
pygame.display.set_caption("Arena")

running = True
player = Player()
pressed = {}
while running:

    screen.blit(background, (0, 0))
    screen.blit(player.image, player.rect)
    pygame.display.flip()
    pygame.display.flip()
    if pressed.get(pygame.K_d):
        player.move_right()
    if pressed.get(pygame.K_q):
        player.move_left()
    if pressed.get(pygame.K_SPACE):
        player.jump()
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            pressed[event.key] = False





