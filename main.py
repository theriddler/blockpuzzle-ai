# Example file showing a circle moving on screen
import pygame
import random

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)

# consts
BLOCK_SIZE = 60
BLOCKS_IN_WIDTH = 10
BLOCKS_IN_HEIGHT = 10

PIXEL_WIDTH = BLOCK_SIZE * BLOCKS_IN_WIDTH
PIXEL_HEIGHT = BLOCK_SIZE * BLOCKS_IN_HEIGHT

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
    BIG_L_TOP_LEFT,
    BIG_L_TOP_RIGHT,
    BIG_L_BOTTOM_LEFT,
    BIG_L_BOTTOM_RIGHT
]

# instantiate a board for us to keep track
board = [[0 for x in range(BLOCKS_IN_WIDTH)] for y in range(BLOCKS_IN_HEIGHT)]

def choose_block():
  return random.choice(blocks)

def draw_board():
  # grid
  for x in range(0, PIXEL_HEIGHT, BLOCK_SIZE):
      pygame.draw.line(screen, WHITE, (x, 0), (x, PIXEL_HEIGHT))
  for y in range(0, PIXEL_WIDTH, BLOCK_SIZE):
      pygame.draw.line(screen, WHITE, (0, y), (PIXEL_WIDTH, y))
    
  # already placed pieces
  for xIdx in range(0, BLOCKS_IN_WIDTH):
    for yIdx in range(0, BLOCKS_IN_WIDTH):
       if(board[yIdx][xIdx] == 1):
          pygame.draw.rect(screen, WHITE, ((xIdx*BLOCK_SIZE), (yIdx*BLOCK_SIZE), BLOCK_SIZE, BLOCK_SIZE))

def mousepos_to_block_top_left(mousePos):
  (mouseX,mouseY) = mousePos

  # get to the root of the block (top left)
  x = mouseX - (mouseX%BLOCK_SIZE)
  y = mouseY - (mouseY%BLOCK_SIZE)

  return (x, y)


def draw_current_block(mousePos, currentBlock):
  (x, y) = mousepos_to_block_top_left(mousePos)

  for yIdx in range(0,3):
      for xIdx in range(0,3):
          if(currentBlock[yIdx][xIdx] == 1):
            pygame.draw.rect(screen, WHITE, ((x+((xIdx-1)*BLOCK_SIZE)), (y+((yIdx-1)*BLOCK_SIZE)), BLOCK_SIZE, BLOCK_SIZE))


def set_current_block(mousePos, currentBlock):
  (x, y) = mousepos_to_block_top_left(mousePos)

  for yIdx in range(0,3):
      for xIdx in range(0,3):
          if(currentBlock[yIdx][xIdx] == 1):
            board[int(y/BLOCK_SIZE)+(yIdx-1)][int(x/BLOCK_SIZE)+(xIdx-1)] = 1
   
  print(board)



# pygame setup
pygame.init()
screen = pygame.display.set_mode((BLOCK_SIZE*BLOCKS_IN_WIDTH, BLOCK_SIZE*BLOCKS_IN_HEIGHT))
clock = pygame.time.Clock()
running = True

currentBlock = BIG_L_BOTTOM_LEFT

while running:
  
  # pygame.QUIT event means the user clicked X to close your window
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
        
      if event.type == pygame.MOUSEBUTTONUP:
        set_current_block(pygame.mouse.get_pos(), currentBlock)

  # set our background
  screen.fill(BLACK)
  draw_board()

  # draw current rect
  draw_current_block(pygame.mouse.get_pos(), currentBlock)

  # no idea why we need this
  pygame.display.flip()
  clock.tick()

pygame.quit()