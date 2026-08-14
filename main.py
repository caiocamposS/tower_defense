# Example file showing a basic pygame "game loop"
import pygame

from src.entities.enemy import Enemy
from src.entities.tower import Tower
from src.entities.projectile import Projectile
from src.entities.map import Map


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

projectile = Projectile()

tower = Tower(5, 5, 1.0, projectile, 240, 160)

tower.image = pygame.transform.scale(tower.image,
                                     (tower.image.get_width() / 3,
                                      tower.image.get_height() / 3))

enemy = Enemy(1, 5)

enemy.image = pygame.transform.scale(enemy.image, 
                                     (enemy.image.get_width() / 12,
                                      enemy.image.get_height() / 12))

map = Map(enemy.image.get_width(), enemy.image.get_height())

running = True

enemy_passed = False
is_map_render = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE

    # renderiza o mapa com rect
    path_group = map.create_group()

    for rect in path_group:
        pygame.draw.rect(screen, "white", rect)

    # movimento do inimigo e se passar perde vida
    if enemy.movement():
        screen.blit(enemy.image, (enemy.position))
        enemy_hitbox = pygame.Rect(enemy.position[0], enemy.position[1], enemy.image.get_width(), enemy.image.get_height())

    elif enemy_passed == False:
        print("Perdeu uma vida.")
        enemy_passed = True

    # posiciona a torre
    screen.blit(tower.image, (tower.position_x, tower.position_y))
    tower_hitbox = pygame.Rect(tower.position_x, tower.position_y, tower.image.get_width(), tower.image.get_height())
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
