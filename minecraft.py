import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Function to generate random green shades
def random_green():
    return (random.randint(0, 100), random.randint(150, 255), random.randint(0, 100))

# Player variables
player_x, player_y = 375, 250  # Starting position
player_width, player_height = 50, 50  # Player dimensions
player_color = (255, 0, 0)  # Red player color
player_speed = 5  # Speed of movement

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with blue for the sky
    screen.fill((135, 206, 235))  # Sky

    # Draw terrain blocks with random shades of green
    for i in range(0, 800, 50):
        for j in range(300, 600, 50):
            pygame.draw.rect(screen, random_green(), (i, j, 50, 50))

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_d] and player_x < 800 - player_width:
        player_x += player_speed
    if keys[pygame.K_w] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_d] and player_y < 600 - player_height:
        player_y += player_speed

    # Draw the player
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
