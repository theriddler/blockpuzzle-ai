# Example file showing a circle moving on screen
import pygame
import random

# block types
# read left to right, top to bottom
SINGLE = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

DOUBLE_LEFT = [
  [0,0,0],
  [1,1,0],
  [0,0,0]
]

DOUBLE_RIGHT = [
  [0,0,0],
  [0,1,1],
  [0,0,0]
]

SQUARE = [
  [0,0,0],
  [1,1,0],
  [1,1,0]
]

BIG_L_TOP_LEFT = [
  [1,1,1],
  [1,0,0],
  [1,0,0]
]

BIG_L_TOP_RIGHT = [
  [1,1,1],
  [0,0,1],
  [0,0,1]
]

BIG_L_BOTTOM_LEFT = [
  [1,0,0],
  [1,0,0],
  [1,1,1]
]

BIG_L_BOTTOM_RIGHT = [
  [0,0,1],
  [0,0,1],
  [1,1,1]
]

blocks = [
    SINGLE,
    DOUBLE_LEFT,
    DOUBLE_RIGHT,
    SQUARE,
    BIG_L_TOP_LEFT,
    BIG_L_TOP_RIGHT,
    BIG_L_BOTTOM_LEFT,
    BIG_L_BOTTOM_RIGHT
]

def choose_block():
  return random.choice(blocks)

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)

# consts
BLOCK_SIZE = 60
BLOCKS_IN_WIDTH = 10
BLOCKS_IN_HEIGHT = 10

PIXEL_WIDTH = BLOCK_SIZE * BLOCKS_IN_WIDTH
PIXEL_HEIGHT = BLOCK_SIZE * BLOCKS_IN_HEIGHT

# instantiate a board for us to keep track
board = [[0 for x in range(BLOCKS_IN_WIDTH)] for y in range(BLOCKS_IN_HEIGHT)]

def draw_board():
  # grid
  for x in range(0, PIXEL_HEIGHT, BLOCK_SIZE):
      pygame.draw.line(screen, BLACK, (x, 0), (x, PIXEL_HEIGHT))
  for y in range(0, PIXEL_WIDTH, BLOCK_SIZE):
      pygame.draw.line(screen, BLACK, (0, y), (PIXEL_WIDTH, y))
    
  # already placed pieces
  for xIdx in range(0, BLOCKS_IN_WIDTH):
    for yIdx in range(0, BLOCKS_IN_WIDTH):
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
  

  if(x < lowerXLimit or x > BLOCKS_IN_WIDTH-upperXLimit-1):
     return False

  if(y < lowerYLimit or y > BLOCKS_IN_HEIGHT-upperYLimit-1):
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

def clear_rows_cols():
  for x in range(0,BLOCKS_IN_WIDTH):
    for y in range(0,BLOCKS_IN_HEIGHT):
       if(board[y][x] != 1):
          break
       
       if(y == BLOCKS_IN_HEIGHT-1):
          for yToClear in range(0,BLOCKS_IN_HEIGHT):
             board[yToClear][x] = 0
          
       
  for y in range(0,BLOCKS_IN_HEIGHT):
    for x in range(0,BLOCKS_IN_WIDTH):
       if(board[y][x] != 1):
          break
       
       if(x == BLOCKS_IN_WIDTH-1):
          for xToClear in range(0,BLOCKS_IN_HEIGHT):
             board[y][xToClear] = 0

  return False

# pygame setup
pygame.init()
screen = pygame.display.set_mode((BLOCK_SIZE*BLOCKS_IN_WIDTH, BLOCK_SIZE*BLOCKS_IN_HEIGHT))
clock = pygame.time.Clock()

running = True
currentBlock = choose_block()

# main loop
while running:

  mousePos = pygame.mouse.get_pos()
  canSetBlock = can_set_current_block(mousePos, currentBlock)
  
  # pygame.QUIT event means the user clicked X to close your window
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
  clear_rows_cols()

  # draw current rect
  if(canSetBlock):
    draw_current_block(mousePos, currentBlock)

  # no idea why we need this
  pygame.display.flip()
  clock.tick()

pygame.quit()