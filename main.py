import pygame

import fire
from Player import Player
from fire import Projectile

pygame.init()

pygame.display.set_caption("Arena")
size = 1080, 720
screen = pygame.display.set_mode(size)
background = pygame.image.load('asset-background2D/_PNG/1/background.png')
background = pygame.transform.scale(background, (1080, 720))
pygame.display.set_caption("Arena")

running = True
player = Player()
Fire = Projectile(player)
pressed = {}
image_path = ['asset-champ2d/PNG/Knight/Walk/walk1.png']
attaque_player = False
attaque_playerAvancement = 7
attaque_playerAcceleration = 0
course = False
while running:
    # anime le changement d'image pour pas qu'il soit trop rapide
    # charge la map
    screen.blit(background, (0, 0))
    # charge la course animé si le joueur est en train de courir ou non
    if course:
        if attaque_player == False:
            image = pygame.transform.scale(player.image, (210, 210))
            player.animate()
            screen.blit(image, player.rect)
    else:
        if attaque_player == False:
            image = pygame.image.load(image_path[0])
            image = pygame.transform.scale(image, (210, 210))
            screen.blit(image, player.rect)
        else:
            if attaque_playerAvancement == 14:
                attaque_playerAvancement = 7
                attaque_player = False
            player.animate_attaque(attaque_playerAvancement)
            image = pygame.transform.scale(player.image, (210, 210))
            attaque_playerAcceleration += 1
            if attaque_playerAcceleration==5:
                attaque_playerAvancement += 1
                attaque_playerAcceleration = 0
            screen.blit(image, player.rect)
    pygame.display.flip()
    pygame.display.flip()
    # condition si certaine touche sont maintenu
    if pressed.get(pygame.K_d):
        player.move_right()
    if pressed.get(pygame.K_q):
        player.move_left()
    if pressed.get(pygame.K_q) or pressed.get(pygame.K_d):
        course = True
    else:
        course = False
    if attaque_player == True:
        course = False
    if pressed.get(pygame.K_SPACE):
        player.jump()
    if pressed.get(pygame.K_s) and player.rect.y < 470:
        player.Unjump()
    if not pressed.get(pygame.K_SPACE) and player.rect.y < 470:
        player.Unjump()
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            pressed[event.key] = True
            # condition si on touche la touche mais ne rentre  dans aucune boucle
            if event.key == pygame.K_g:
                player.launch_projectile()
            if event.key == pygame.K_e:
                attaque_player = True
        elif event.type == pygame.KEYUP:
            pressed[event.key] = False
    # permet de faire bouger notre projectile
    for projectile in player.all_projectile:
        projectile.animate()
        projectile.move(player)
    # dessine tout les projectiles présent sur la map
    player.all_projectile.draw(screen)
    pygame.display.flip()
