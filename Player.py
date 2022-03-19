import pygame
from fire import Projectile


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.health = 100
        self.max_health = 100
        self.attack = 20
        self.velocity = 12
        self.jumpp = 7
        self.animationimage = load_animation_images_P('run')
        self.anim = 0
        self.image = self.animationimage[self.anim]
        self.image = pygame.transform.scale(self.image, (210, 210))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 490
        self.vitesseanim = 0
        self.all_projectile = pygame.sprite.Group()

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def jump(self):
        self.rect.y -= self.jumpp * 2

    def Unjump(self):
        self.rect.y += self.jumpp * 1.5

    def launch_projectile(self):
        projectile = Projectile
        self.all_projectile.add(Projectile(self))

    def animate(self):
        if self.anim == 7:
            self.anim = 0
        self.vitesseanim += 1
        if self.vitesseanim == 6:
            self.anim += 1
            self.vitesseanim = 0
            self.image = self.animationimage[self.anim]

    def animate_attaque(self, avancement_image):
        self.image = self.animationimage[avancement_image]


def load_animation_images_P(sprite_name):
    images = []
    path = f"asset-champ2d/PNG/Knight/Run/run"
    path_attaque = f"asset-champ2d/PNG/Knight/Attack_Extra/attack_extra"
    for num in range(1, 9):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))
    for num in range(1, 9):
        image_path = path_attaque + str(num) + '.png'
        images.append(pygame.image.load(image_path))
    return images
