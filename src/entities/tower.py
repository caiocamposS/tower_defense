import pygame

from src.entities.projectile import Projectile

image_path = "/home/caio-breno/projects/tower_defense/assets/images/tower.png"


class Tower(pygame.sprite.Sprite):
    def __init__(
        self, range: int, damage: int, cooldown: float, projectile: Projectile, position_x: int, position_y: int
    ):
        pygame.sprite.Sprite.__init__(self)

        self.range = range
        self.damage = damage
        self.cooldown = cooldown
        self.projectile = projectile

        self.position_x = position_x
        self.position_y = position_y

        self.image = pygame.image.load(image_path).convert_alpha()

    def attack():
        pass
