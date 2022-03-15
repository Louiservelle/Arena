import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.health = 100
        self.max_health = 100
        self.attack = 20
        self.velocity = 9
        self.jumpp = 10
        self.image = pygame.image.load('asset-champ2d/PNG/Knight/knight.png')
        self.image = pygame.transform.scale(self.image, (210, 210))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 490
        self.all_projectile = pygame.sprite.Group()

    def move_right(self):

        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def jump(self):
        self.rect.y -= self.jumpp
