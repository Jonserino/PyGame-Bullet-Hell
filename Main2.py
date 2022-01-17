import pygame as pg
from Sprites import *

width = 1200
height = 800
middle = (width/2, height/2)
fps = 60

black = (0, 0, 0)
white = (255, 255, 255)
gray = (127.5, 127.5, 127.5)
light_gray = (175, 175, 175)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

class Game():
    def __init__(self):
        pg.init()
        
        
        self.comic_sans30 = pg.font.SysFont("Comic Sams MS", 30)
        
        self.screen = pg.display.set_mode((width, height))
        self.clock = pg.time.Clock()
        
        self.points = 0
        self.text_you_died = self.comic_sans30.render('You Died', False, red)

        
        self.new()
    
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.projectiles = pg.sprite.Group()
        
        self.my_player = Player()
        self.all_sprites.add(self.my_player)
    
        self.my_shield = Shield(self.my_player)
        self.all_sprites.add(self.my_shield)

        self.run()
        
    def run(self):
        self.playing = True
        while self.playing: # Game Loop
            self.clock.tick(fps)
            self.events()    
            self.update()
            self.draw()
            
        self.new()
    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    self.playing = False
                    pg.quit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    self.playing = False
                    self.new()
        

        
    def update(self):
        self.all_sprites.update()
        
        self.hits = pg.sprite.spritecollide(self.my_player, self.enemies, True)
        while len(self.enemies) < 1:
            knight = Enemy(self)
            self.all_sprites.add(knight)
            self.enemies.add(knight)
            self.points += 1
        self.hits2 = pg.sprite.spritecollide(self.my_player, self.projectiles, True)
        while len(self.projectiles) < 2:
            fireball = Fireball(self)
            self.all_sprites.add(fireball)
            self.projectiles.add(fireball)
            self.points += 1
        self.hits3 = pg.sprite.spritecollide(self.my_player, self.projectiles, True)
        while len(self.projectiles) < 2:
            arrow = Arrow(self)
            self.all_sprites.add(arrow)
            self.projectiles.add(arrow)
            self.points += 1
        self.block = pg.sprite.spritecollide(self.my_shield, self.enemies, True)
        while len(self.enemies) < 1:
            knight = Enemy(self)
            self.all_sprites.add(knight)
            self.enemies.add(knight)
        self.block2 = pg.sprite.spritecollide(self.my_shield, self.projectiles, True)
        while len(self.projectiles) < 2:
            fireball = Fireball(self)
            self.all_sprites.add(fireball)
            self.projectiles.add(fireball)
        self.block3 = pg.sprite.spritecollide(self.my_shield, self.projectiles, True)
        while len(self.projectiles) < 2:
            arrow = Arrow(self)
            self.all_sprites.add(arrow)
            self.projectiles.add(arrow)
        
        if self.hits:
            self.my_player.health -= knight.attack
        if self.hits2:
            self.my_player.health -= fireball.attack
        if self.my_player.health <= 0:
            self.screen.blit(self.text_you_died, middle)


    
    def draw(self):
        self.screen.fill(black)

        self.all_sprites.draw(self.screen)

        self.text_player_hp = self.comic_sans30.render(str(self.my_player.health) + 'HP', False, red)

        self.screen.blit(self.text_player_hp, (10, 5))

        print("Hits", self.points)
        
        pg.display.update()
        
g = Game()

