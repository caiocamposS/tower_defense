import pygame

from game.path import PATH
from src.entities.enemy import Enemy

class Map(pygame.sprite.Sprite):
    def __init__(self, enemy_width: int, enemy_height: int, path: list[int] = PATH, width: int = 70):
        self.enemy_width = enemy_width
        self.enemy_height = enemy_height

        self.path = path
        self.width = width

    def create_group(self):
        path_rect1 = pygame.Rect(self.path[0][0], self.path[0][1], self.path[1][0] + self.enemy_width, self.width)
        path_rect2 = pygame.Rect(self.path[1][0], self.path[1][1], self.width, (self.path[2][1] - self.path[1][1]) + self.enemy_height)
        path_rect3 = pygame.Rect(self.path[3][0], self.path[3][1], (self.path[2][0] - self.path[3][0]) + self.enemy_width, self.width)
        path_rect4 = pygame.Rect(self.path[4][0], self.path[4][1], self.width, self.path[3][1] + self.enemy_height)

        return [path_rect1,
                path_rect2,
                path_rect3,
                path_rect4]