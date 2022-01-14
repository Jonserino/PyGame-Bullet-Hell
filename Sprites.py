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
        self.health = 10

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

    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = enemy_image
        self.image = pg.transform.scale(self.image, (250, 225))
        self.rect = self.image.get_rect()
        self.pos = vec(1000, randint(0, 600))
        self.rect.center = self.pos
        self.life = 10
        self.speed_x = 1
        self.speed_y = 1
        self.attack = 10

    def update(self):
        self.pos.x += self.speed_x
        self.pos.y += self.speed_y

     
            
        if self.game.my_player.pos.x < self.pos.x:
            self.speed_x = -1
        if self.game.my_player.pos.x > self.pos.x:
            self.speed_x = 1
        if self.game.my_player.pos.y < self.pos.y:
            self.speed_y = -1
        if self.game.my_player.pos.y > self.pos.y:
            self.speed_y = 1
            


        self.rect.center = self.pos


class Fireball(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = fireball_image
        self.image = pg.transform.scale(self.image, (40, 35))
        self.image_up_right = pg.transform.rotate(self.image, 45)
        self.image_down_right = pg.transform.rotate(self.image, 45)
        self.image_up_left = pg.transform.rotate(self.image, 45)
        self.image_down_left = pg.transform.rotate(self.image, 45)
        self.rect = self.image.get_rect()
        self.pos = vec(1400, randint(0, 600))
        self.rect.center = self.pos
        self.life = 2
        self.speed_x = 1
        self.speed_y = 1
        self.attack = 1
        self.up = False
        self.right = False

    def update(self):
        self.pos.x += self.speed_x
        self.pos.y += self.speed_y


        if self.pos.x > 1200:
            self.speed_x = -5
            self.image = pg.transform.flip(self.image, True, False)
            self.right = False
        if self.pos.x < 0:
            self.speed_x = 5
            self.image = pg.transform.flip(self.image, True, False)
            self.right = True
        if self.pos.y > 800:
            self.speed_y = -5
            self.image = pg.transform.flip(self.image, False, True)
            self.image = pg.transform.flip(self.image, True, False)
        if self.pos.y < 0:
            self.speed_y = 5
            self.image = pg.transform.flip(self.image, False, True)
            self.image = pg.transform.flip(self.image, True, False)
        if self.up and self.right:
            self.image = self.image_up_right   
        if not self.up and self.right:
            self.image = self.image_down_left 
        
        

        self.rect.center = self.pos
