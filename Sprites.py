import pygame as pg
vec = pg.math.Vector2
from random import randint

enemy_image = pg.image.load("enemy.png")
player_image = pg.image.load("heart.png")
fireball_image = pg.image.load("fireball.png")
fireball_image_up = pg.image.load("fireball_up.png")
fireball_image_down = pg.image.load("fireball_down.png")
fireball_image_left = pg.image.load("fireball_left.png")
fireball_image_right = pg.image.load("fireball_right.png")
shield_image = pg.image.load("shield.png")
shield_image_up = pg.image.load("shield_up.png")
shield_image_down = pg.image.load("shield_down.png")
shield_image_left = pg.image.load("shield_left.png")
shield_image_right = pg.image.load("shield_right.png")
'''
arrow_image = pg.image.load(".png")
arrow_image_up = pg.image.load(".png")
arrow_image_down = pg.image.load(".png")
arrow_image_left = pg.image.load(".png")
arrow_image_right = pg.image.load(".png")
'''

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = player_image
        self.image = pg.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.pos = vec(600, 400)
        self.rect.center = self.pos
        self.speed = 2.5
        self.health = 10

    def update(self):
        keys = pg.key.get_pressed()
        '''
        if keys[pg.K_a] and self.pos.x > self.speed:
            self.pos.x -= self.speed
        if keys[pg.K_d] and self.pos.x < 995:
            self.pos.x += self.speed
        if keys[pg.K_w] and self.pos.y > self.speed:
            self.pos.y -= self.speed
        if keys[pg.K_s] and self.pos.y < 795:
            self.pos.y += self.speed
        '''
        self.rect.center = self.pos

class Shield(pg.sprite.Sprite):
    def __init__(self, player):
        pg.sprite.Sprite.__init__(self)
        self.player = player
        self.image = shield_image
        self.image_up = shield_image_up
        self.image_down = shield_image_down
        self.image_left = shield_image_left
        self.image_right = shield_image_right
        self.image = pg.transform.scale(self.image, (110, 20))
        self.image_up = pg.transform.scale(self.image_up, (110, 20))
        self.image_down = pg.transform.scale(self.image_down, (110, 20))
        self.image_left = pg.transform.scale(self.image_left, (20, 110))
        self.image_right = pg.transform.scale(self.image_right, (20, 110))
        self.rect = self.image.get_rect()
        self.pos = vec(600, 350)
        self.rect.center = self.pos

    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.pos.x = 550
            self.pos.y = 400
            self.image = self.image_left
            self.rect = self.image.get_rect()
        if keys[pg.K_RIGHT]:
            self.pos.x = 650
            self.pos.y = 400
            self.image = self.image_right
            self.rect = self.image.get_rect()
        if keys[pg.K_UP]:
            self.pos.x = 600
            self.pos.y = 350
            self.image = self.image_up
            self.rect = self.image.get_rect()
        if keys[pg.K_DOWN]:
            self.pos.x = 600
            self.pos.y = 450
            self.image = self.image_down
            self.rect = self.image.get_rect()

        self.rect.center = self.pos


class Enemy(pg.sprite.Sprite):

    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = enemy_image
        self.image = pg.transform.scale(self.image, (250, 225))
        self.rect = self.image.get_rect()
        self.pos = vec(1200, 400)
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

    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = fireball_image
        self.image_up = fireball_image_up
        self.image_down = fireball_image_down
        self.image_left = fireball_image_left
        self.image_right = fireball_image_right
        self.image = pg.transform.scale(self.image, (40, 35))
        self.image_up = pg.transform.scale(self.image_up, (35, 40))
        self.image_down = pg.transform.scale(self.image_down, (35, 40))
        self.image_left = pg.transform.scale(self.image_right, (40, 35))
        self.image_right = pg.transform.scale(self.image_left, (40, 35))
        self.rect = self.image.get_rect()
        self.pos = vec(600, 10)
        self.rect.center = self.pos
        self.life = 2
        self.speed_x = 3
        self.speed_y = 3
        self.attack = 1
        self.up = False
        self.right = False

    def update(self):
        self.pos.x += self.speed_x
        self.pos.y += self.speed_y


        if self.game.my_player.pos.x < self.pos.x:
            self.speed_x = -3
            self.image = self.image_left
            self.rect = self.image.get_rect()
        if self.game.my_player.pos.x > self.pos.x:
            self.speed_x = 3
            self.image = self.image_right
            self.rect = self.image.get_rect()
        if self.game.my_player.pos.y < self.pos.y:
            self.speed_y = -3
            self.image = self.image_up
            self.rect = self.image.get_rect()
        if self.game.my_player.pos.y > self.pos.y:
            self.speed_y = 3
            self.image = self.image_down
            self.rect = self.image.get_rect()
        
        

        self.rect.center = self.pos
'''
class Arrow(pg.sprite.Sprite):
    
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = arrow_image
        self.image_up = arrow_image_up
        self.image_down = arrow_image_down
        self.image_left = arrow_image_left
        self.image_right = arrow_image_right
        self.image = pg.transform.scale(self.image, (40, 35))
        self.image_up = pg.transform.scale(self.image_up, (35, 40))
        self.image_down = pg.transform.scale(self.image_down, (35, 40))
        self.image_left = pg.transform.scale(self.image_right, (40, 35))
        self.image_right = pg.transform.scale(self.image_left, (40, 35))
        self.rect = self.image.get_rect()
        self.pos = vec(600, 200)
        self.rect.center = self.pos
        self.life = 2
        self.speed_x = 3
        self.speed_y = 3
        self.attack = 1
        self.up = False
        self.right = False

    def update(self):
        self.pos.x += self.speed_x
        self.pos.y += self.speed_y


        if self.game.my_player.pos.x < self.pos.x:
            self.speed_x = -3
            self.image = self.image_left
            self.rect = self.image.get_rect()
        if self.game.my_player.pos.x > self.pos.x:
            self.speed_x = 3
            self.image = self.image_right
            self.rect = self.image.get_rect()
        if self.game.my_player.pos.y < self.pos.y:
            self.speed_y = -3
            self.image = self.image_up
            self.rect = self.image.get_rect()
        if self.game.my_player.pos.y > self.pos.y:
            self.speed_y = 3
            self.image = self.image_down
            self.rect = self.image.get_rect()
        
        

        self.rect.center = self.pos
'''