import pygame
from blocks import *

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)

# board params
BLOCK_SIZE = 60 #px

BOARD_WIDTH = 10
BOARD_HEIGHT = 10

SCREEN_WIDTH = BLOCK_SIZE*BOARD_WIDTH
SCREEN_HEIGHT = BLOCK_SIZE*BOARD_HEIGHT

# pygame setup
pygame.init()
screen = pygame.display.set_mode((BLOCK_SIZE*BOARD_WIDTH, BLOCK_SIZE*BOARD_HEIGHT))


class Blockpuzzle(object):
  def __init__(self):
    self.running = True
    self.inputStack = []
    self.currentBlock = choose_block()
    self.board = [[0 for x in range(BOARD_WIDTH)] for y in range(BOARD_HEIGHT)]

  def draw_board(self):
    screen.fill(WHITE)
    
    # grid
    for x in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (SCREEN_WIDTH, y))
      
    # already placed pieces
    for xIdx in range(0, BOARD_WIDTH):
      for yIdx in range(0, BOARD_WIDTH):
        if(self.board[yIdx][xIdx] == 1):
            xStart = (xIdx*BLOCK_SIZE)
            yStart = (yIdx*BLOCK_SIZE)
            pygame.draw.rect(screen, BLACK, (xStart, yStart, BLOCK_SIZE, BLOCK_SIZE))


  def mousepos_to_board_indexes(self,mousePos):
    (mouseX,mouseY) = mousePos

    # get to the root of the block (top left)
    x = (mouseX - (mouseX%BLOCK_SIZE)) / BLOCK_SIZE
    y = (mouseY - (mouseY%BLOCK_SIZE)) / BLOCK_SIZE

    return (int(x), int(y))


  def draw_current_block(self, mousePos):
    (x, y) = self.mousepos_to_board_indexes(mousePos)

    for yIdx in range(0,3):
        for xIdx in range(0,3):
            if(self.currentBlock[yIdx][xIdx] == 1):
              xStart = ((x+xIdx-1)*BLOCK_SIZE)
              yStart = ((y+yIdx-1)*BLOCK_SIZE)
              pygame.draw.rect(screen, BLACK, (xStart, yStart, BLOCK_SIZE, BLOCK_SIZE))


  def can_place_current_block(self, mousePos):
    (x, y) = self.mousepos_to_board_indexes(mousePos)

    lowerXLimit = 0
    upperXLimit = 0
    lowerYLimit = 0
    upperYLimit = 0
    
    for idx in range(0,3):
      if(self.currentBlock[idx][0] == 1):
        lowerXLimit = 1
      
      if(self.currentBlock[idx][2] == 1):
        upperXLimit = 1

      if(self.currentBlock[0][idx] == 1):
        lowerYLimit = 1
      
      if(self.currentBlock[2][idx] == 1):
        upperYLimit = 1
    

    if(x < lowerXLimit or x > BOARD_WIDTH-upperXLimit-1):
      return False

    if(y < lowerYLimit or y > BOARD_HEIGHT-upperYLimit-1):
      return False
    
    for yIdx in range(0,3):
        for xIdx in range(0,3):
            if(self.currentBlock[yIdx][xIdx] == 1):
              if(self.board[y+yIdx-1][x+xIdx-1] == 1):
                return False
    
    return True

  def place_current_block(self, mousePos):
    (x, y) = self.mousepos_to_board_indexes(mousePos)

    for yIdx in range(0,3):
        for xIdx in range(0,3):
            if(self.currentBlock[yIdx][xIdx] == 1):
              self.board[y+yIdx-1][x+xIdx-1] = 1

  def clear_full_rows(self):               
    for y in range(0,BOARD_HEIGHT):
      for x in range(0,BOARD_WIDTH):
        if(self.board[y][x] != 1):
            break
        
        if(x == BOARD_WIDTH-1):
            for xToClear in range(0,BOARD_HEIGHT):
              self.board[y][xToClear] = 0

  def clear_full_cols(self):
    for x in range(0,BOARD_WIDTH):
      for y in range(0,BOARD_HEIGHT):
        if(self.board[y][x] != 1):
            break
        
        if(y == BOARD_HEIGHT-1):
            for yToClear in range(0,BOARD_HEIGHT):
                self.board[yToClear][x] = 0

  def frame(self, mousePos, click):
    canSetBlock = self.can_place_current_block(mousePos)

    # set our board as per current state
    self.clear_full_rows()
    self.clear_full_cols()
    self.draw_board()

    # draw current rect
    if(canSetBlock):
      self.draw_current_block(mousePos)

    if(click and canSetBlock):
      self.place_current_block(mousePos)
      self.currentBlock = choose_block()

    # no idea why we need this
    pygame.display.flip()
     