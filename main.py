# Example file showing a basic pygame "game loop"
import pygame

from src.entities.enemy import Enemy


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

enemy = Enemy(1, 5)

enemy.image = pygame.transform.scale(enemy.image, 
                                     (enemy.image.get_width() / 12,
                                      enemy.image.get_height() / 12))

running = True

# waypoints
PATH = [[-enemy.image.get_width(), 150],[1000, 150],[1000, 550],[280, 550],[280, -enemy.image.get_height()]]

enemy_pos = list(PATH[0])
target_idx = 1

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE

    if target_idx < len(PATH):
        target_pos = PATH[target_idx]

        if enemy_pos[0] < target_pos[0]:
            enemy_pos[0] += enemy.speed
        elif enemy_pos[0] > target_pos[0]:
            enemy_pos[0] -= enemy.speed

        if enemy_pos[1] < target_pos[1]:
            enemy_pos[1] += enemy.speed
        elif enemy_pos[1] > target_pos[1]:
            enemy_pos[1] -= enemy.speed

        if enemy_pos == target_pos:
            target_idx += 1

    else:
        print("Perdeu uma vida")


    screen.blit(enemy.image, (enemy_pos))
    hitbox = pygame.Rect(enemy_pos[0], enemy_pos[1], enemy.image.get_width(), enemy.image.get_height())

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
