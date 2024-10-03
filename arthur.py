import pygame
from bike import *
from player import Player

pygame.init()

# Set the window size and title
win_width = 1270
win_height = 720
game_window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Moving Object Using PyGame")
canvas = pygame.Surface((win_width, win_height))
clock = pygame.time.Clock()
TARGET_FPS = 60

# Create player instance
player = Player()

# Need a starting point for the player
obj_width = win_width
obj_height = 10
obj_x = 10
obj_y = 720 // 2 - 12
obj_speed = 30

running = True
while running:
    dt = clock.tick(60) * .001 * TARGET_FPS

    # Quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.LEFT_KEY, player.FACING_LEFT = True, True
            elif event.key == pygame.K_RIGHT:
                player.RIGHT_KEY, player.FACING_LEFT = True, True
            elif event.key == pygame.K_SPACE:
                player.jump()

        # Check for key releases
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.LEFT_KEY = False
            elif event.key == pygame.K_RIGHT:
                player.RIGHT_KEY = False
            elif event.key == pygame.K_SPACE:
                if player.is_jumping:
                    player.velocity.y *= .25
                    player.is_jumping = False

    player.update(dt)

    game_window.fill((0, 1, 1))

    # Draw the player and other elements
    player.draw(game_window)
    pygame.draw.rect(game_window, (150, 255, 0), (obj_x, obj_y, obj_width, obj_height))

    # Update the display once per frame
    pygame.display.flip()
