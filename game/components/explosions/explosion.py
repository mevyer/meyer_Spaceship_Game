import pygame
from pygame.sprite import Sprite

from game.utils.constants import EXPLOSION


class Explosion(Sprite):
    
    def __init__(self, spaceship):
        self.image = EXPLOSION
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center
        self.life = pygame.time.get_ticks() + 200

    def update(self):
        self.rect.y += 10

    def draw(self, screen):
        screen.blit(self.image, self.rect)
