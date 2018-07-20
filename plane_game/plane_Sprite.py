import random
from plane_constant import *


class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, speed = 1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class Background(GameSprite):

    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= WINDOW.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):

    def __init__(self):
        super().__init__("./images/enemy1.png")
        self.speed = random.randint(1, 3)
        self.rect.bottom = 0
        self.rect.x = random.randint(0, WINDOW.width-self.rect.width)

    def update(self):
        super().update()
        if self.rect.y >= WINDOW.height:
            self.kill()


class Hero(GameSprite):

    def __init__(self):
        super().__init__("./images/me1.png", 0)
        self.rect.centerx = WINDOW.centerx
        self.rect.bottom = WINDOW.bottom - 120
        self.bullet_group = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        self.speed = 0
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > WINDOW.right:
            self.rect.right = WINDOW.right

    def fire(self):
        for i in (0, 20, 40):
            bullet = Bullet()
            bullet.rect.bottom = self.rect.y - i
            bullet.rect.centerx = self.rect.centerx
            self.bullet_group.add(bullet)


class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./images/bullet1.png", -2)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()
