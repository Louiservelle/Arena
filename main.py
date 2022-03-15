import pygame

pygame.init()

pygame.display.set_caption("Arena")
size = 1080, 720
screen = pygame.display.set_mode(size)
background = pygame.image.load('asset-background2D/_PNG/1/background.png')
pygame.display.set_caption("Arena")
running = True

while running:

    screen.blit(background, (0, 0))

    pygame.display.flip()
    for even in pygame.event.get():
        if even.Type == pygame.QUIT:
            running = False
            pygame.quit()



