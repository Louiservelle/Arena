import pygame

pygame.init()

screen = pygame.display.set_mode(1080, 720)
background = pygame.image.load('asset-background2D/_PNG/1/background.png')
pygame.display.set_caption("Arena")
running = True

while running:
    screen.blit(background())