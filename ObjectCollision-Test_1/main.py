import pygame 
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        # initialize game window, etc
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

    def load(self):
        # Spawn the Logs
        for i in range(2):
            # Logs on Row 1
            self.logs_1 = LogRows(neg_logspeed, SPACING_3, i+1, 288, LOG_WIDTH)
            self.all_sprites.add(self.logs_1)
            self.logsleft.add(self.logs_1)
            
        # Spawn the player
        self.player = Player(self)
        self.all_sprites.add(self.player)
        
    def new(self):
        # start a new game
        self.all_sprites = pygame.sprite.Group()
        self.logsleft = pygame.sprite.Group()
        self.load()
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()

        # check if the player goes off the screen
        if self.player.rect.left <= 0:
            self.player.rect.left = 0
        if self.player.rect.right >= 480:
            self.player.rect.right = 480
        if self.player.rect.bottom >= HEIGHT - 96:
            self.player.rect.bottom = HEIGHT - 96
        if self.player.rect.bottom <= 48:
            self.player.rect.bottom = HEIGHT - 96

        # check if player hits a log
        self.logsleft_hit = pygame.sprite.spritecollide(self.player, self.logsleft, False, pygame.sprite.collide_rect)
        if len(self.logsleft_hit) != 0:
            self.player.onLog = True

    def events(self):
        # Game Loop - events
        for event in pygame.event.get():
            # Checking for Player events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.speedx = -48
                if event.key == pygame.K_RIGHT:
                    self.player.speedx = 48
                if event.key == pygame.K_UP:
                    self.player.speedy = -48
                if event.key == pygame.K_DOWN:
                    self.player.speedy = 48

            if event.type == pygame.KEYUP:#and self.onLog == False:
                if event.key == pygame.K_LEFT:
                    self.player.speedx = 0
                if event.key == pygame.K_RIGHT:
                    self.player.speedx = 0
                if event.key == pygame.K_UP:
                    self.player.speedy = 0
                if event.key == pygame.K_DOWN:
                    self.player.speedy = 0

            self.player.rect.x += self.player.speedx
            self.player.rect.y += self.player.speedy
            # check for closing window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pygame.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pygame.quit()
