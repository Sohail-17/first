import pygame
import random
import math
import sys
import os


pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Environment with Red Block")

RED = (255, 0, 0)
DARK_RED = (139, 0, 0)
BLACK = (0, 0, 0)
BLOCK_SIZE = 50
NUM_BLOCKS = 75
Bee = pygame.image.load("sahur.jpg")

camera_x, camera_y = 0, 0
camera_zoom = 500
camera_tilt_x, camera_tilt_y = 0, 0

blocks = [Bee]
for _ in range(NUM_BLOCKS):
    x = random.randint(-WIDTH // 2, WIDTH // 2)
    y = random.randint(-HEIGHT // 2, HEIGHT // 2)
    z = random.randint(1, 500)
    blocks.append([x, y, z])

pygame.mouse.set_visible(True)
pygame.event.set_grab(False)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit the loop when the quit event is detected

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        camera_y -= 10
    if keys[pygame.K_s]:
        camera_y += 10
    if keys[pygame.K_a]:
        camera_x -= 10
    if keys[pygame.K_d]:
        camera_x += 10
    if keys[pygame.K_q]:
        camera_zoom += 10
    if keys[pygame.K_e]:
        camera_zoom -= 10
    if keys[pygame.K_ESCAPE]:
        running = False 
    mouse_dx, mouse_dy = pygame.mouse.get_rel()
    camera_tilt_x += mouse_dx * 0.2
    camera_tilt_y += mouse_dy * 0.2

    screen.fill(BLACK)
    for block in blocks:
        x, y, z = block
        tilt_x_rad = math.radians(camera_tilt_x)
        tilt_y_rad = math.radians(camera_tilt_y)
        y_rotated = y * math.cos(tilt_y_rad) - z * math.sin(tilt_x_rad)
        z_rotated = y * math.sin(tilt_y_rad) + z * math.cos(tilt_y_rad)
        x_rotated = x * math.cos(tilt_x_rad) + z_rotated * math.sin(tilt_x_rad)
        z_rotated = -x * math.sin(tilt_x_rad) + z_rotated * math.cos(tilt_x_rad)
        scale = camera_zoom / (camera_zoom + z_rotated)
        screen_x = int(WIDTH // 2 + (x_rotated - camera_x) * scale)
        screen_y = int(HEIGHT // 2 + (y_rotated - camera_y) * scale)
        size = int(BLOCK_SIZE * scale)
        pygame.draw.rect(screen, RED, (screen_x, screen_y, size, size))
        top_color = DARK_RED
        top_points = [
            (screen_x, screen_y),
            (screen_x + size, screen_y),
            (screen_x + size - int(size * 0.3), screen_y - int(size * 0.3)),
            (screen_x - int(size * 0.3), screen_y - int(size * 0.3)),
        ]
        pygame.draw.polygon(screen, top_color, top_points)
        side_color = DARK_RED
        side_points = [
            (screen_x + size, screen_y),
            (screen_x + size, screen_y + size),
            (screen_x + size - int(size * 0.3), screen_y + size - int(size * 0.3)),
            (screen_x + size - int(size * 0.3), screen_y - int(size * 0.3)),
        ]
        pygame.draw.polygon(screen, side_color, side_points)
        block[2] -= 2
        if block[2] <= 0:
            block[2] = random.randint(100, 500)
    pygame.display.flip()
    clock.tick(75)
BULLET_COLOR = (255, 255, 0)
BULLET_SPEED = 20
bullets = []
def shoot_bullet():
    bullets.append([WIDTH // 2, HEIGHT // 2, 0])
if pygame.mouse.get_pressed()[0]:
    shoot_bullet()
for bullet in bullets[:]:
    bullet[2] += BULLET_SPEED
    bullet_scale = camera_zoom / (camera_zoom + bullet[2])
    bullet_x = int(WIDTH // 2)
    bullet_y = int(HEIGHT // 2)
    bullet_size = int(5 * bullet_scale)
    pygame.draw.circle(screen, BULLET_COLOR, (bullet_x, bullet_y), bullet_size)
    for block in blocks[:]:
        block_scale = camera_zoom / (camera_zoom + block[2])
        block_screen_x = int(WIDTH // 2 + (block[0] - camera_x) * block_scale)
        block_screen_y = int(HEIGHT // 2 + (block[1] - camera_y) * block_scale)
        block_size = int(BLOCK_SIZE * block_scale)
        if(block_screen_x < bullet_x < block_screen_x + block_size and block_screen_y < bullet_y < block_screen_y + block_size):
            blocks.remove(block)
            bullets.remove(bullet)
            break
        if bullet[2] > 500:
            bullets.remove(bullet)
            pygame.quit()

