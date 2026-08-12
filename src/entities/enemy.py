import pygame

image_path = "/home/caio-breno/projects/tower_defense/assets/images/enemy.png"

class Enemy(pygame.sprite.Sprite):
    def __init__(self, life: int, speed: int):
        pygame.sprite.Sprite.__init__(self)

        self.life = life
        self.speed = speed
        
        self.image = pygame.image.load(image_path).convert_alpha()
