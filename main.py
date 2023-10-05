# Example file showing a circle moving on screen
import pygame
from blocks import *

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)

# consts
BLOCK_SIZE = 60 #px

BOARD_WIDTH = 10
BOARD_HEIGHT = 10

PIXEL_WIDTH = BLOCK_SIZE*BOARD_WIDTH
PIXEL_HEIGHT = BLOCK_SIZE*BOARD_HEIGHT

# instantiate a board for us to keep track
board = [[0 for x in range(BOARD_WIDTH)] for y in range(BOARD_HEIGHT)]

def draw_board():
  # grid
  for x in range(0, PIXEL_HEIGHT, BLOCK_SIZE):
      pygame.draw.line(screen, BLACK, (x, 0), (x, PIXEL_HEIGHT))
  for y in range(0, PIXEL_WIDTH, BLOCK_SIZE):
      pygame.draw.line(screen, BLACK, (0, y), (PIXEL_WIDTH, y))
    
  # already placed pieces
  for xIdx in range(0, BOARD_WIDTH):
    for yIdx in range(0, BOARD_WIDTH):
       if(board[yIdx][xIdx] == 1):
          xStart = (xIdx*BLOCK_SIZE)
          yStart = (yIdx*BLOCK_SIZE)
          pygame.draw.rect(screen, BLACK, (xStart, yStart, BLOCK_SIZE, BLOCK_SIZE))


def mousepos_to_board_indexes(mousePos):
  (mouseX,mouseY) = mousePos

  # get to the root of the block (top left)
  x = (mouseX - (mouseX%BLOCK_SIZE)) / BLOCK_SIZE
  y = (mouseY - (mouseY%BLOCK_SIZE)) / BLOCK_SIZE

  return (int(x), int(y))


def draw_current_block(mousePos, currentBlock):
  (x, y) = mousepos_to_board_indexes(mousePos)

  for yIdx in range(0,3):
      for xIdx in range(0,3):
          if(currentBlock[yIdx][xIdx] == 1):
            xStart = ((x+xIdx-1)*BLOCK_SIZE)
            yStart = ((y+yIdx-1)*BLOCK_SIZE)
            pygame.draw.rect(screen, BLACK, (xStart, yStart, BLOCK_SIZE, BLOCK_SIZE))


def can_set_current_block(mousePos, currentBlock):
  (x, y) = mousepos_to_board_indexes(mousePos)

  lowerXLimit = 0
  upperXLimit = 0
  lowerYLimit = 0
  upperYLimit = 0
  
  for idx in range(0,3):
    if(currentBlock[idx][0] == 1):
      lowerXLimit = 1
    
    if(currentBlock[idx][2] == 1):
      upperXLimit = 1

    if(currentBlock[0][idx] == 1):
      lowerYLimit = 1
    
    if(currentBlock[2][idx] == 1):
      upperYLimit = 1
  

  if(x < lowerXLimit or x > BOARD_WIDTH-upperXLimit-1):
     return False

  if(y < lowerYLimit or y > BOARD_HEIGHT-upperYLimit-1):
     return False
  
  for yIdx in range(0,3):
      for xIdx in range(0,3):
          if(currentBlock[yIdx][xIdx] == 1):
            if(board[y+yIdx-1][x+xIdx-1] == 1):
              return False
  
  return True

def set_current_block(mousePos, currentBlock):
  (x, y) = mousepos_to_board_indexes(mousePos)

  for yIdx in range(0,3):
      for xIdx in range(0,3):
          if(currentBlock[yIdx][xIdx] == 1):
            board[y+yIdx-1][x+xIdx-1] = 1

def clear_full_rows():               
  for y in range(0,BOARD_HEIGHT):
    for x in range(0,BOARD_WIDTH):
       if(board[y][x] != 1):
          break
       
       if(x == BOARD_WIDTH-1):
          for xToClear in range(0,BOARD_HEIGHT):
             board[y][xToClear] = 0

def clear_full_cols():
  for x in range(0,BOARD_WIDTH):
    for y in range(0,BOARD_HEIGHT):
       if(board[y][x] != 1):
          break
       
       if(y == BOARD_HEIGHT-1):
          for yToClear in range(0,BOARD_HEIGHT):
             board[yToClear][x] = 0

# pygame setup
pygame.init()
screen = pygame.display.set_mode((BLOCK_SIZE*BOARD_WIDTH, BLOCK_SIZE*BOARD_HEIGHT))
clock = pygame.time.Clock()

running = True
currentBlock = choose_block()

# main loop
while running:

  # operational variables
  mousePos = pygame.mouse.get_pos()
  canSetBlock = can_set_current_block(mousePos, currentBlock)
  
  # event handler
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
        
      if event.type == pygame.MOUSEBUTTONUP:
        if(canSetBlock):
          set_current_block(mousePos, currentBlock)
          currentBlock = choose_block()

  # set our board as per current state
  screen.fill(WHITE)
  draw_board()
  clear_full_rows()
  clear_full_cols()

  # draw current rect
  if(canSetBlock):
    draw_current_block(mousePos, currentBlock)

  # no idea why we need this
  pygame.display.flip()
  clock.tick()

pygame.quit()