import pygame
import random
import math

# Initialize
pygame.init()
screen = pygame.display.set_mode((400, 600))
clock = pygame.time.Clock()

# Bird setup
bird_x = 100
bird_y = 300
bird_vel = 0

# Rock setup
rock_x = 400
rock_y_base = 250
rock_speed = 4

# Game loop
running = True
time_counter = 0
while running:
    screen.fill((135, 206, 235))  # Sky blue
    time_counter += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update bird
    bird_vel += 0.5  # gravity
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bird_vel = -7
    bird_y += bird_vel

    # Update rock
    rock_x -= rock_speed
    if rock_x < -50:
        rock_x = 400
        rock_y_base = random.randint(200, 400)

    # Float effect using sine wave
    rock_y = rock_y_base + 20 * math.sin(time_counter * 0.05)

    # Draw
    pygame.surface.Surface((bird_x, bird_y))

    pygame.surface.Surface((rock_x, rock_y))

    # Collision detection
    bird_rect = pygame.Rect(bird_x, bird_y)
    rock_rect = pygame.Rect(rock_x, rock_y)
    if bird_rect.colliderect(rock_rect):
        print("Hit!")
        running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
