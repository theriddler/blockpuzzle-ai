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

SNAKE_LEFT = [
  [0,0,0],
  [0,1,1],
  [1,1,0]
]

SNAKE_RIGHT= [
  [0,0,0],
  [1,1,0],
  [0,1,1]
]

SNAKE_UP= [
  [1,0,0],
  [1,1,0],
  [0,1,0]
]

SNAKE_DOWN= [
  [0,1,0],
  [1,1,0],
  [1,0,0]
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

NOZZLE_DOWN = [
  [0,0,1],
  [0,0,1],
  [1,1,1]
]

blocks = [
    SINGLE,
    DOUBLE_LEFT,
    DOUBLE_RIGHT,
    SQUARE,
    SNAKE_LEFT,
    SNAKE_RIGHT,
    SNAKE_UP,
    SNAKE_DOWN,
    BIG_L_TOP_LEFT,
    BIG_L_TOP_RIGHT,
    BIG_L_BOTTOM_LEFT,
    BIG_L_BOTTOM_RIGHT
]

def choose_block():
  return random.choice(blocks)