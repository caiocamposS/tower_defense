import pygame
from game.path import PATH

image_path = "/home/caio-breno/projects/tower_defense/assets/images/enemy.png"

class Enemy(pygame.sprite.Sprite):
    def __init__(self, life: int, speed: int, path: list[int] = PATH, position: list[int] = PATH[0], target_pos_idx: int = 1):
        pygame.sprite.Sprite.__init__(self)

        self.life = life
        self.speed = speed
        self.path = path
        self.position = position
        self.target_idx = target_pos_idx
        
        self.image = pygame.image.load(image_path).convert_alpha()

    def movement(self):
        if self.target_idx >= len(self.path):
            return False

        target_x, target_y = self.path[self.target_idx]

        if self.position[0] < target_x:
            self.position[0] += self.speed

            if self.position[0] > target_x:
                self.position[0] = target_x

        elif self.position[0] > target_x:
            self.position[0] -= self.speed

            if self.position[0] < target_x:
                self.position[0] = target_x

        elif self.position[1] < target_y:
            self.position[1] += self.speed

            if self.position[1] > target_y:
                self.position[1] = target_y

        elif self.position[1] > target_y:
            self.position[1] -= self.speed

            if self.position[1] < target_y:
                self.position[1] = target_y

        if self.position == [target_x, target_y]:
            self.target_idx += 1

        return True