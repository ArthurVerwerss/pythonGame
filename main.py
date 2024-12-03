import pygame
from player import Player
from spritesheet.spritesheet import Spritesheet
from tiles import *

pygame.init()

# Set the window size and title
win_width = 1270
win_height = 720
game_window = pygame.display.set_mode((win_width, win_height))
canvas = pygame.Surface((win_width, win_height))
clock = pygame.time.Clock()
TARGET_FPS = 60

# Create player instance
player = Player()
spritesheet = Spritesheet('spritesheet.png')
map = TileMap('test_level.csv', spritesheet)
player.position.x, player.position.y = map.start_x, map.start_y

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

    player.update(dt, map.tiles)

    canvas.fill((0, 180, 240))
    map.draw_map(canvas)
    player.draw(canvas)
    game_window.blit(canvas, (0, 0))
    pygame.display.update()
