import time
import pygame
from blocks import *
from Blockpuzzle import Blockpuzzle

if __name__ == '__main__':
  blockpuzzle = Blockpuzzle()
  clock = pygame.time.Clock()

  # main loop
  while blockpuzzle.running:

    # operational variables
    mousePos = pygame.mouse.get_pos()
    click = False

    # event handler
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        blockpuzzle.running = False
        
      if event.type == pygame.MOUSEBUTTONUP:
        click = True

    blockpuzzle.frame(mousePos, click)
    clock.tick()
      
  pygame.quit()
    