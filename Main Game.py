import pygame as pg
import time
from Sprites import *
from Settings import *
import sys
import os
import pygame.freetype

pg.init()
pg.font.init()

width = 1200
height = 800

middle = (width/2, height/2)

black = (0, 0, 0)
white = (255, 255, 255)
gray = (127.5, 127.5, 127.5)
light_gray = (175, 175, 175)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

menu_pos_x = 0
menu_pos_y = 360
menu_size_x = 800
menu_size_y = 240

button1_pos_x = 20
button1_pos_y = 400
button1_size_x = 195
button1_size_y = 60

gray_bar_size_x = width
gray_bar_size_y = 35
gray_bar_pos_x = 0
gray_bar_pos_y = 0

direction = 1

comic_sans30 = pg.font.SysFont('Comic Sans MS', 30)

screen = pg.display.set_mode((width, height))

menu = (menu_pos_x, menu_pos_y, menu_size_x, menu_size_y)
button1 = (button1_pos_x, button1_pos_y, button1_size_x, button1_size_y)
gray_bar = (gray_bar_pos_x, gray_bar_pos_y, gray_bar_size_x, gray_bar_size_y)

clock = pg.time.Clock()
fps = 300

all_sprites = pg.sprite.Group()
enemies = pg.sprite.Group()
fireballs = pg.sprite.Group()

knight = Enemy()
all_sprites.add(knight)
enemies.add(knight)

player = Player()
all_sprites.add(player)

fireball = Fireball()
all_sprites.add(fireball)
fireballs.add(fireball)

points = -1

text_you_died = comic_sans30.render('You Died', False, red)

toggle = False
playing = True
while playing:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_TAB:
                if not toggle:
                    toggle = True
                else:
                    toggle = False

    screen.fill(black)
    keys = pg.key.get_pressed()

    if keys[pg.K_ESCAPE]:
        playing = False
    if keys[pg.K_q]:
        playing = False
    if toggle:
        pg.draw.rect(screen, white, menu)
        pg.draw.rect(screen, gray, button1)

    pg.draw.rect(screen, gray, gray_bar)

    all_sprites.update()

    hits = pg.sprite.spritecollide(player, enemies, True)
    while len(enemies) < 1:
        knight = Enemy()
        all_sprites.add(knight)
        enemies.add(knight)
        points += 1
    hits2 = pg.sprite.spritecollide(player, fireballs, True)
    while len(fireballs) < 2:
        fireball = Fireball()
        all_sprites.add(fireball)
        fireballs.add(fireball)
        points += 1

    if hits:
        player.health -= knight.attack
    if hits2:
        player.health -= fireball.attack
    if player.health <= 0:
        screen.blit(text_you_died, middle)

    text_player_hp = comic_sans30.render(str(player.health) + 'HP', False, red)

    screen.blit(text_player_hp, (10, 5))

    all_sprites.draw(screen)

    print("hits", points)

    pg.display.update()

pg.quit()

