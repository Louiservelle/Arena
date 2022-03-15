import pygame

pygame.init()

pygame.display.set_caption("Arena")
size = 1080, 720
screen = pygame.display.set_mode(size)
background = pygame.image.load('asset-background2D/_PNG/1/background.png')
background = pygame.transform.scale(background, (1080, 720))
pygame.display.set_caption("Arena")
running = True
while running:

    screen.blit(background, (0, 0))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()



