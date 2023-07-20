import pygame

class ExplosionManager:
    def __init__(self):
        self.explosions = []

    def update(self):
        for explosion in self.explosions:
            explosion.update()

            now = pygame.time.get_ticks()
            if now >= explosion.life:
                self.explosions.remove(explosion)
                

    def draw(self, screen):
        for explosion in self.explosions:
            explosion.draw(screen)

    def add_explosion(self, explosion):
        self.explosions.append(explosion)

    def reset(self):
        self.explosions = []
