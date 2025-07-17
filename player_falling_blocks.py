import pygame
import sys
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()
running = True
dt = 0
pygame.display.set_caption('Falling Blocks')
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() - 100)
def game_loop():
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((105, 186, 255))

        pygame.draw.circle(screen, "red", player_pos, 30)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player_pos.x -= 150 * dt
        if keys[pygame.K_d]:
            player_pos.x += 150 * dt

        pygame.display.flip()

        dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit
game_loop()
pygame.quit()
