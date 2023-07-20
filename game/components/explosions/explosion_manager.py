import pygame

class ExplosionManager:
    def __init__(self):
        self.explosions = []

    def update(self, game):
        for explosion in self.explosions:
            explosion.update()

            now = pygame.time.get_ticks()
            if now >= explosion.life:
                if explosion.owner == 'player':
                    game.game_over()
                else:
                    self.explosions.remove(explosion)
                

    def draw(self, screen):
        for explosion in self.explosions:
            explosion.draw(screen)

    def add_explosion(self, explosion):
        explosion.sound.play()
        self.explosions.append(explosion)

    def reset(self):
        self.explosions = []
