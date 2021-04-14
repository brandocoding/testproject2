import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 96
        self.speedx = 0
        self.speedy = 0
        self.onLog = False

    def update(self):
        if self.onLog:
            self.speedx = neg_logspeed
            self.speedy = 0
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            print(self.onLog)

class LogRows(pygame.sprite.Sprite):
    def __init__(self, speed, spacing, start_x, bottom, width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = (start_x * (spacing + BOX_WIDTH))
        self.rect.bottom = bottom
        self.speedx = speed

    def update(self):
        self.rect.x += self.speedx
        if self.rect.x < -30:
            self.rect.x = 480
        if self.rect.x > 480:
            self.rect.x = -30
        
        
