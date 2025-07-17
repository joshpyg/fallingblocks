import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Blocks")

BLACK = (0, 0, 0)
RED = (255, 0, 0)

BLOCK_SIZE = 45
FALL_SPEED = 2
SPAWN_INTERVAL = 40

clock = pygame.time.Clock()

blocks = []  

frame_count = 0
shake_time = 0

running = True
while running:
    clock.tick(60)
    frame_count += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if frame_count >= SPAWN_INTERVAL:
        x = random.randint(0, WIDTH - BLOCK_SIZE)
        y = 0
        landed = False
        timer = 60
        blocks.append([x, y, landed, timer])
        frame_count = 0

    for i in range(len(blocks)):
        if blocks[i][2] == False:
            blocks[i][1] += FALL_SPEED
            if blocks[i][1] + BLOCK_SIZE >= HEIGHT:
                blocks[i][1] = HEIGHT - BLOCK_SIZE
                blocks[i][2] = True
                shake_time = 10
        else:
            blocks[i][3] -= 1

    blocks = [b for b in blocks if b[3] > 0]

    if shake_time > 0:
        offset_x = random.randint(-5, 5)
        offset_y = random.randint(-5, 5)
        shake_time -= 1
    else:
        offset_x = 0
        offset_y = 0

    win.fill(BLACK)
    for b in blocks:
        pygame.draw.rect(win, RED, (b[0] + offset_x, b[1] + offset_y, BLOCK_SIZE, BLOCK_SIZE))

    pygame.display.update()

pygame.quit()
