import pygame 
  
background_colour = (0, 128, 0) 
  
screen = pygame.display.set_mode((1270, 700)) 
  
pygame.display.set_caption('Geeksforgeeks') 
  
screen.fill(background_colour) 
  
pygame.display.flip() 
  
running = True
  
while running: 
    for event in pygame.event.get():       
        if event.type == pygame.QUIT: 
            running = False