import pygame

bike_image = pygame.image.load('bike.png')
bike_image = pygame.transform.scale(bike_image, (120, 100))

def bike(game_window, win_width, obj_y):
    game_window.blit(bike_image, (win_width // 2, obj_y - 100))
