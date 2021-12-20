import pygame as pg
vec = pg.math.Vector2
from random import randint


enemy_image = pg.image.load("enemy.png")
player_image = pg.image.load("heart.png")
fireball_image = pg.image.load("fireball.png")


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = player_image
        self.image = pg.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.pos = vec(100, 100)
        self.rect.center = self.pos
        self.speed = 2.5
        self.health = 5

    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_a] and self.pos.x > self.speed:
            self.pos.x -= self.speed
        if keys[pg.K_d] and self.pos.x < 995:
            self.pos.x += self.speed
        if keys[pg.K_w] and self.pos.y > self.speed:
            self.pos.y -= self.speed
        if keys[pg.K_s] and self.pos.y < 795:
            self.pos.y += self.speed

        self.rect.center = self.pos


class Enemy(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_image
        self.image = pg.transform.scale(self.image, (250, 225))
        self.rect = self.image.get_rect()
        self.pos = vec(1400, randint(0, 600))
        self.rect.center = self.pos
        self.life = 10
        self.speed_x = 1
        self.speed_y = 1
        self.attack = 10

    def update(self):
        self.pos.x += self.speed_x
        self.pos.y += self.speed_y

        if self.pos.x > 1200:
            self.speed_x = -1
        if self.pos.x < 0:
            self.speed_x = 1
        if self.pos.y > 800:
            self.speed_y = -1
        if self.pos.y < 0:
            self.speed_y = 1

        self.rect.center = self.pos


class Fireball(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = fireball_image
        self.image = pg.transform.scale(self.image, (40, 35))
        self.rect = self.image.get_rect()
        self.pos = vec(1400, randint(0, 600))
        self.rect.center = self.pos
        self.life = 2
        self.speed_x = 1
        self.speed_y = 1
        self.attack = 1

    def update(self):
        self.pos.x += self.speed_x
        self.pos.y += self.speed_y

        if self.pos.x > 1200:
            self.speed_x = -5
        if self.pos.x < 0:
            self.speed_x = 5
        if self.pos.y > 800:
            self.speed_y = -5
        if self.pos.y < 0:
            self.speed_y = 5

        self.rect.center = self.pos
