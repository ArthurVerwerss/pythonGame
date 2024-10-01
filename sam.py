import pygame
from bike import *
pygame.init()

# Set the window size and title
win_width = 1270
win_height = 720
game_window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Moving Object Using PyGame")

# Set up the object size, dimensions and speed
obj_width = 30
obj_height = 30
obj_x = 10
obj_y = win_height // 2
obj_speed = 30
bike = pygame.image.load('bike.png')
bike = pygame.transform.scale(bike, (120, 100))
bg = pygame.image.load('background.jpg')
bg = pygame.transform.scale(bg, (win_width, win_height))

running = True
while running:
#    quit event
   for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    # checks on key inputs
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT]:        
        obj_x -= obj_speed
    if keys[pygame.K_RIGHT]:          
        obj_x += obj_speed
        
    # draws the rectangle
   game_window.fill((0, 1, 1))
   game_window.blit(bg, (0, 0))
   drawline(game_window, win_height, obj_width, win_width)
#    pygame.draw.rect(game_window, (150, 255, 0), (obj_x, obj_y, obj_width, obj_height))
   game_window.blit(bike, (obj_x, obj_y + -63))
   pygame.display.flip()
pygame.quit()
