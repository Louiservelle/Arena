import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.velocity = 10
        self.animation = load_animation_images('fire')
        self.anim = 0
        self.image = self.animation[self.anim]
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 130
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.distance = 0
        self.acceleration = 0

    def animate(self):
        self.acceleration += 1
        if self.anim < 7 and self.acceleration == 8:
            self.anim += 1
            self.acceleration = 0
            self.image = self.animation[self.anim]
            self.image = pygame.transform.scale(self.image, (100, 100))

    def move(self, player):
        self.rect.x += self.velocity
        self.distance += self.velocity
        if self.distance == 650:
            self.remove()

    def remove(self):
        self.player.all_projectile.remove(self)


def load_animation_images(sprite_name):
    images = []
    path = f"asset-champ2d/PNG/Mage/Fire/fire"

    for num in range(1, 10):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))
    return images
