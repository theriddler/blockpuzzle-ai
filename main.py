# Example file showing a circle moving on screen
import pygame
import random

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)

# consts
BLOCK_SIZE = 60
BLOCK_IN_X = 10
BLOCK_IN_Y = 10

width = BLOCK_SIZE * BLOCK_IN_X
height = BLOCK_SIZE * BLOCK_IN_Y

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

def choose_block():
  return random.choice(blocks)

def draw_grid():
    for x in range(0, height, BLOCK_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, height))
    for y in range(0, width, BLOCK_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (width, y))

def draw_current_block(mousePos, currentBlock):
    (mouseX,mouseY) = mousePos

    # get to the root of the block (top left)
    xStart = mouseX - (mouseX%BLOCK_SIZE)
    yStart = mouseY - (mouseY%BLOCK_SIZE)

    for y in range(0,2):
        for x in range(0,2):
            occupied = currentBlock[yIdx][xIdx]
            print(occupied)
            if(occupied == 1):
              pygame.draw.rect(screen, WHITE, (xStart-BLOCK_SIZE, y, BLOCK_SIZE, BLOCK_SIZE))


# pygame setup
pygame.init()
screen = pygame.display.set_mode((BLOCK_SIZE*BLOCK_IN_X, BLOCK_SIZE*BLOCK_IN_Y))
clock = pygame.time.Clock()
running = True

currentBlock = DOUBLE_RIGHT
print(currentBlock)

while running:
  
  # pygame.QUIT event means the user clicked X to close your window
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False

  # set our background
  screen.fill(BLACK)
  draw_grid()

  # draw current rect
  draw_current_block(pygame.mouse.get_pos(), currentBlock)

  # no idea why we need this
  pygame.display.flip()
  clock.tick()

pygame.quit()