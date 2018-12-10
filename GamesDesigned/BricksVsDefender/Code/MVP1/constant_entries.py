"""
  This file contains all constant variables.

  @author Vivek Vellaiyappan Surulimuthu | vivekvellaiyappans@gmail.com
"""

# Screen Size
SCREEN_SIZE = (640, 480)

# Color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (200, 200, 0)
RED = (220, 0, 0)
GREEN = (0, 128, 0)
ORANGE = (255, 128, 0)
VIOLET = (255, 0, 255)
HOT_PINK = (255, 105, 180)
BROWN_FADED = (138, 78, 55)

BRICK_COLOR = BROWN_FADED
PADDLE_COLOR = RED
BALL_COLOR = BLACK
POW_MAX_LIFE_BRICK_COLOR = ORANGE
POW_PADDLE_COLOR = VIOLET

# Brick Dimensions
BRICK_WIDTH = 60
BRICK_HEIGHT = 15
BRICKS_ROW = 1
BRICKS_COLUMN = 8

# Paddle Dimensions
PADDLE_WIDTH = 70
POW_PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15
PADDLE_SPEED_LEFT = 15
PADDLE_SPEED_RIGHT = 15

# Ball Dimensions
BALL_SPEED = [4, -4]
BALL_DIAMETER = 16
BALL_RADIUS = int(BALL_DIAMETER / 2)

# Max movement of entities inside screen
MAX_PADDLE_X = SCREEN_SIZE[0] - PADDLE_WIDTH
MAX_BALL_X = SCREEN_SIZE[0] - BALL_DIAMETER
MAX_BALL_Y = SCREEN_SIZE[1] - BALL_DIAMETER

# Paddle location on screen
PADDLE_Y = SCREEN_SIZE[1] - PADDLE_HEIGHT - 20

# Game State
STATE_BALL_IN_PADDLE = 0
STATE_PLAYING = 1
STATE_WON = 2
STATE_GAME_OVER = 3

MAX_LIFE = 3
MAX_SCORE_PER_BRICK = 10

AUDIO_FILE_LOCATION = 'bing_audio.wav'


def call():
    pass


if __name__ == "__main__":
    call()