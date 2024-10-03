import pygame
from spritesheet import Spritesheet

pygame.init()

# Set the window size and title
win_width = 1270
win_height = 720
game_window = pygame.display.set_mode((win_width, win_height))
canvas = pygame.Surface((win_width, win_height))
pygame.display.set_caption("Moving Object Using PyGame")

my_spritesheet = Spritesheet('spritesheet/bike_sheet.png')
bikes = [my_spritesheet.parse_sprite('bike_color.png'), my_spritesheet.parse_sprite('bike2.png')]
index = 0

running = True
while running:

    # Quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                index = (index + 1) % len(bikes)

    canvas.fill((255,255,255))
    canvas.blit(bikes[index], (0, win_height - 288))
    game_window.blit(canvas, (0,0))
    pygame.display.update()

pygame.quit()
