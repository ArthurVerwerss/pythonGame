import pygame
from bike import *
pygame.init()

# Set the window size and title
win_width = 1270
win_height = 720
game_window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Moving Object Using PyGame")

obj_width = win_width
obj_height = 10
obj_x = 10
obj_y = 720 // 2 + 30
obj_speed = 30


running = True
while running:
#    quit event
   for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    # checks on key inputs
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT]:        
        obj_x += obj_speed
    if keys[pygame.K_RIGHT]:          
        obj_x -= obj_speed
        
    # draws the rectangle
    game_window.fill((0, 1, 1))
    bike(game_window, win_width, obj_y)
    pygame.draw.rect(game_window, (150, 255, 0), (obj_x, obj_y, obj_width,    obj_height))
    pygame.display.flip()
pygame.quit()