from json import load
import pygame
background_colour = (255,255,255)
(width, height) = (1080, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)
#pygame.display.flip()
running = True


stickman= pygame.image.load("stickman.png")
screen.blit(stickman, (100,100))


while running:
  
  for event in pygame.event.get():
    
    
    
    if event.type == pygame.QUIT:
      running = False