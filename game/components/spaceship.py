import pygame
from pygame.sprite import Sprite

from game.components.bullets.bullet import Bullet
from game.components.bullets.bullet_manager import BulletManager
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, SHIP_WIDTH, SHIP_HEIGHT

class Spaceship(Sprite):
    X_POS = (SCREEN_WIDTH // 2) - SHIP_WIDTH
    Y_POS = 500
    SHIP_SPEED = 10
    
    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (SHIP_WIDTH, SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

        self.score = 0
        self.highest_score = 0
        self.death_count = 0

        self.type = 'player'
        self.last_shoot_time = 0
        self.shooting_interval = 250

    def update(self, user_input, game):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()
        if user_input[pygame.K_SPACE]:
            self.shoot(game.bullet_manager)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shoot_time >= self.shooting_interval:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.last_shoot_time = current_time

    def move_left(self):
        self.rect.x -= self.SHIP_SPEED
        if self.rect.left < -70:
            self.rect.x = SCREEN_WIDTH
    
    def move_right(self):
        self.rect.x += self.SHIP_SPEED
        if self.rect.right > SCREEN_WIDTH + 70:
            self.rect.x = -70

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= self.SHIP_SPEED

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.y += self.SHIP_SPEED
