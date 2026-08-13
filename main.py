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

map_image = pygame.image.load("assets/images/map.png").convert_alpha()
map_image = pygame.transform.scale(map_image,
                                   (screen.get_width(),
                                    screen.get_height()))

running = True

enemy_passed = False

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.blit(map_image, (0, 0))

    # RENDER YOUR GAME HERE

    # movimento do inimigo e se passar perde vida
    if enemy.movement():
        screen.blit(enemy.image, (enemy.position))
        hitbox = pygame.Rect(enemy.position[0], enemy.position[1], enemy.image.get_width(), enemy.image.get_height())

    elif enemy_passed == False:
        print("Perdeu uma vida.")
        enemy_passed = True

    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
