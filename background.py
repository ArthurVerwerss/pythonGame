import pygame
def drawline(game_window, win_height, obj_width, win_width):
    pygame.draw.rect(game_window, (255, 255, 0), (1, win_height // 2 + obj_width, win_width, 10))
