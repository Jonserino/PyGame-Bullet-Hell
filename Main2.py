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
purple = (255, 0, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
light_blue = (10, 175, 255)
dark_green = (10, 150, 75)

class Game():
    def __init__(self):
        pg.init()
        
        
        self.comic_sans25 = pg.font.SysFont("Comic Sams MS", 25)
        self.comic_sans30 = pg.font.SysFont("Comic Sams MS", 30)
        self.comic_sans35 = pg.font.SysFont("Comic Sams MS", 35)
        self.comic_sans40 = pg.font.SysFont("Comic Sams MS", 40)
        self.comic_sans45 = pg.font.SysFont("Comic Sams MS", 45)
        self.comic_sans50 = pg.font.SysFont("Comic Sams MS", 50)
        
        self.screen = pg.display.set_mode((width, height), pg.FULLSCREEN)
        self.clock = pg.time.Clock()
        

        
        self.start_screen()
    
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.moving_sprites = pg.sprite.Group()
        
        self.enemies = pg.sprite.Group()
        self.arrows = pg.sprite.Group()
        self.fireballs = pg.sprite.Group()
        
        self.firewall = pg.sprite.Group()
        self.all_sprites.add(self.firewall)
        self.moving_sprites.add(self.firewall)
        
        self.my_player = Player()
        self.all_sprites.add(self.my_player)
        
        self.my_shield = Shield(self.my_player)
        self.all_sprites.add(self.my_shield)
        
        self.difficulty = 3
        self.difficulty_amount = 10
        self.increase_difficulty = False
        self.points = 0


        self.run()
        
    def newhard(self):
        self.all_sprites = pg.sprite.Group()
        
        self.moving_sprites = pg.sprite.Group()
        self.firewall1 = Firewall(self, 600, 800)
        self.firewall2 = Firewall(self, 0, 800)
        self.firewall3 = Firewall(self, 1200, 800)
        self.moving_sprites.add(self.firewall1, self.firewall2, self.firewall3)
        
        self.enemies = pg.sprite.Group()
        self.arrows = pg.sprite.Group()
        self.fireballs = pg.sprite.Group()
        self.firewalls = pg.sprite.Group()
                
        self.my_player = Player()
        self.all_sprites.add(self.my_player)
        
        self.my_shield = Shield(self.my_player)
        self.all_sprites.add(self.my_shield)
        
        self.difficulty = 6
        self.difficulty_amount = 20
        self.increase_difficulty = False
        self.points = 0


        self.runhard()

    def run(self):
        self.playing = True
        while self.playing: # Game Loop
            self.clock.tick(fps)
            self.events()    
            self.update()
            self.draw()
            
        self.new()

    def runhard(self):
        self.playing = True
        while self.playing: # Game Loop
            self.clock.tick(fps)
            self.events()    
            self.update()
            self.draw()
            
        self.newhard()

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
     
        self.hits2 = pg.sprite.spritecollide(self.my_player, self.arrows, True)
        
        self.hits3 = pg.sprite.spritecollide(self.my_player, self.fireballs, True)

        self.block = pg.sprite.spritecollide(self.my_shield, self.enemies, True)
   
        self.block3 = pg.sprite.spritecollide(self.my_shield, self.arrows, True)
        
        self.block3 = pg.sprite.spritecollide(self.my_shield, self.fireballs, True)

        while len(self.fireballs) < 2:
            self.fireball = Fireball(self)
            self.all_sprites.add(self.fireball)
            self.fireballs.add(self.fireball)
            self.points += 1      
            
  
        while len(self.enemies) < 1:
            self.knight = Enemy(self)
            self.all_sprites.add(self.knight)
            self.enemies.add(self.knight)
            self.points += 1    
            
    
      
        while len(self.arrows) < 2:
            self.arrow = Arrow(self)
            self.all_sprites.add(self.arrow)
            self.arrows.add(self.arrow)
            self.points += 1
        

        if self.hits:
            self.my_player.health -= self.knight.attack
        if self.hits3:
            self.my_player.health -= self.fireball.attack
        if self.hits2:
            self.my_player.health -= self.arrow.attack
        if self.my_player.health <= 0:
            self.game_over()
         
        if self.points > self.difficulty_amount:
            self.increase_difficulty = True
 
        if self.increase_difficulty:
            self.difficulty_amount += 100
            self.increase_difficulty = False
            self.difficulty += 1
        
    def draw(self):
        self.screen.fill(black)

        self.all_sprites.draw(self.screen)

        self.text_player_hp = self.comic_sans30.render(str(self.my_player.health) + 'HP', False, red)
        self.text_points = self.comic_sans30.render(str(self.points), False, (red))
        
        self.screen.blit(self.text_player_hp, (10, 5))
        self.screen.blit(self.text_points, (70, 5))

        print("Hits", self.points)
        
        pg.display.update()

    def start_screen(self):
        self.starting = True
        while self.starting:
            self.clock.tick(0)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        pg.quit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:
                        self.new()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_h:
                        self.newhard()
                
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_i:
                        self.info()
            
            self.screen.fill(light_blue)
            
            
            self.text_title = self.comic_sans50.render('Blocking Bullets', False, blue)
            self.text_start = self.comic_sans40.render('Press "R" to Start', False, red)
            self.text_hard = self.comic_sans25.render('Press "H" for Hard Mode', False, purple)
            self.text_info = self.comic_sans35.render('Press "I" for Info', False, green)
            self.text_quit = self.comic_sans30.render('Press "Q" to Quit', False, red)

            self.screen.blit(self.text_title, ((width/2) - (self.text_title.get_width()/2), 200))
            self.screen.blit(self.text_start, ((width/2) - (self.text_start.get_width()/2), 400))
            self.screen.blit(self.text_hard, ((width/2) - (self.text_quit.get_width()/1.70), 450))
            self.screen.blit(self.text_info, ((width/2) - (self.text_info.get_width()/2), 600))
            self.screen.blit(self.text_quit, ((width/2) - (self.text_quit.get_width()/2), 650))

            pg.display.update()
            
    def info(self):
        self.information = True
        while self.information:
            self.clock.tick(0)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        pg.quit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:
                        self.new()
                    
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_f:
                        self.start_screen()
                        
            self.screen.fill(dark_green)
            
            self.text_info = self.comic_sans40.render('Info:', False, green)
            self.text_controls = self.comic_sans30.render('Controls:', False, green)
            self.text_arrows = self.comic_sans30.render('"Arrow Keys to move the Shield"', False, green)
            self.text_goal = self.comic_sans30.render('Goal:', False, green)
            self.text_topic = self.comic_sans30.render('"Block all of the projectiles and last as long as you can!"', False, green)
            self.text_back = self.comic_sans30.render('Press "F" to go back to the Start Screen"', False, green)
            self.text_quit = self.comic_sans30.render('Press "Q" to Quit', False, green)

            self.screen.blit(self.text_info, (10, 10))
            self.screen.blit(self.text_controls, (30, 40))
            self.screen.blit(self.text_arrows, (50, 70))
            self.screen.blit(self.text_goal, (30, 100))
            self.screen.blit(self.text_topic, (50, 130))
            self.screen.blit(self.text_back, (20, 750))
            self.screen.blit(self.text_quit, (20, 700))
            
            pg.display.update()

    def game_over(self):
        self.gameover = True
        while self.gameover:
            self.clock.tick(0)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        pg.quit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:
                        self.new()
                
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_f:
                        self.start_screen()
     
            
            self.screen.fill(black)
            
            self.moving_sprites.draw(self.screen)
            self.moving_sprites.update()
            
            self.text_you_died = self.comic_sans30.render('You Died', False, red)
            self.text_restart = self.comic_sans30.render('Press "R" to Restart', False, red)
            self.text_start = self.comic_sans30.render('Press "F" to go to the Start Screen', False, red)
            self.text_quit = self.comic_sans30.render('Press "Q" to Quit', False, red)

            self.screen.blit(self.text_you_died, ((width/2) - (self.text_you_died.get_width()/2) , 400))
            self.screen.blit(self.text_restart, ((width/2) - (self.text_restart.get_width()/2), 500))
            self.screen.blit(self.text_start, ((width/2) - (self.text_start.get_width()/2), 600))
            self.screen.blit(self.text_quit, ((width/2) - (self.text_quit.get_width()/2), 650))

            
            pg.display.update()
    
g = Game()