"""
Title: Bricks vs Defender
Author: Vivek Vellaiyappan Surulimuthu | vivekvellaiyappans@gmail.com
Proposal Submission Date: 13th September 2018
Project Url: https://github.com/vivekVells/GameDesignProgramming/tree/master/GamesDesigned/BricksVsDefender
Aim:
  Combination of Brick Breaker and Pill ball Game but totally new concept
    that is not available anywhere in internet as of now.
  The game to be developed - titled “Bricks vs Defender” will be a multi-player defending game
    which is based on Last Man Standing gaming concept.
This File Scope:
  For now, brick breaker game alone done. further improvements will be made
Short Note: (Will be doing the following)
  Function creations for redundant operations
  Constant entries file import action
  Image Background
"""

# to execute the .pyc file
# !/usr/bin/python

import sys
import pygame

from . import constant_entries

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


class BrickBreaker(object):
    def __init__(self):
        pygame.init()

        self.done = False
        self.bricks = []
        self.pow_bricks = []
        self.max_lives = None
        self.max_life_brick = None
        self.brick_width_enlarge = None
        self.enlarge_paddle = False
        self.score = None
        self.state = None
        self.paddle = None
        self.pow_paddle_width = None
        self.ball = None
        self.ball_vel = None

        self.audio_play = pygame.mixer.Sound(AUDIO_FILE_LOCATION)
        self.audio_play.set_volume(10)

        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Brick Breaker Game")

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Calibri', 20, True, True)

        self.restart_game()

    def restart_game(self):
        self.bricks = []
        self.pow_bricks = []
        self.enlarge_paddle = False
        self.max_lives = MAX_LIFE
        self.score = 0
        self.state = STATE_BALL_IN_PADDLE
        self.paddle = pygame.Rect(300, PADDLE_Y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.ball = pygame.Rect(300, PADDLE_Y - BALL_DIAMETER, BALL_DIAMETER, BALL_DIAMETER)
        self.ball_vel = BALL_SPEED
        self.create_bricks()

    def create_bricks(self):
        y_ofs = 100

        for i in range(BRICKS_ROW):
            x_ofs = 50
            for j in range(BRICKS_COLUMN):
                self.bricks.append(pygame.Rect(x_ofs, y_ofs, BRICK_WIDTH, BRICK_HEIGHT))
                x_ofs += BRICK_WIDTH + 10
            y_ofs += BRICK_HEIGHT + 5

        # Power up features
        # max lives increase brick
        self.pow_bricks.append(pygame.Rect(SCREEN_SIZE[0]/2, 50, BRICK_WIDTH, BRICK_HEIGHT))
        self.max_life_brick = self.pow_bricks[0]

        # enlarge paddle width brick
        self.pow_bricks.append(pygame.Rect(SCREEN_SIZE[0]/2 - 100, 50, BRICK_WIDTH, BRICK_HEIGHT))
        self.brick_width_enlarge = self.pow_bricks[1]

    def draw_bricks(self):
        for brick in self.bricks:
            pygame.draw.rect(self.screen, BRICK_COLOR, brick)

        for pow_brick in self.pow_bricks:
            if pow_brick == self.max_life_brick:
                pygame.draw.rect(self.screen, POW_MAX_LIFE_BRICK_COLOR, pow_brick)
            elif pow_brick == self.brick_width_enlarge:
                pygame.draw.rect(self.screen, POW_PADDLE_COLOR, pow_brick)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.paddle.left -= PADDLE_SPEED_LEFT
            if self.paddle.left < 0:
                self.paddle.left = 0

        if keys[pygame.K_RIGHT]:
            self.paddle.left += PADDLE_SPEED_RIGHT
            if self.paddle.left > MAX_PADDLE_X:
                self.paddle.left = MAX_PADDLE_X

        if keys[pygame.K_SPACE] and self.state == STATE_BALL_IN_PADDLE:
            self.ball_vel = BALL_SPEED
            self.state = STATE_PLAYING
        elif keys[pygame.K_RETURN] and (self.state == STATE_GAME_OVER or self.state == STATE_WON):
            self.restart_game()

        if keys[pygame.K_BACKSPACE]:
            self.done = True

        if keys[pygame.K_ESCAPE]:
            sys.exit()

    def move_ball(self):
        self.ball.left += self.ball_vel[0]
        self.ball.top += self.ball_vel[1]

        if self.ball.left <= 0:
            self.ball.left = 0
            self.ball_vel[0] = -self.ball_vel[0]
        elif self.ball.left >= MAX_BALL_X:
            self.ball.left = MAX_BALL_X
            self.ball_vel[0] = -self.ball_vel[0]

        if self.ball.top < 0:
            self.ball.top = 0
            self.ball_vel[1] = -self.ball_vel[1]
        elif self.ball.top >= MAX_BALL_Y:
            self.ball.top = MAX_BALL_Y
            self.ball_vel[1] = -self.ball_vel[1]

    def handle_collisions(self):
        for brick in self.bricks:
            if self.ball.colliderect(brick):
                self.audio_play.play(0)
                self.score += MAX_SCORE_PER_BRICK
                self.ball_vel[1] = -self.ball_vel[1]
                self.bricks.remove(brick)
                break

        for pow_brick in self.pow_bricks:
            if self.ball.colliderect(pow_brick):
                if pow_brick == self.pow_bricks[0]:
                    self.pow_bricks.remove(pow_brick)
                    self.max_lives += 1
                elif pow_brick == self.pow_bricks[1]:
                    self.pow_bricks.remove(pow_brick)
                    self.enlarge_paddle = True
                break

        if len(self.bricks) == 0:
            self.state = STATE_WON

        if self.ball.colliderect(self.paddle):
            self.audio_play.play(0)
            self.ball.top = PADDLE_Y - BALL_DIAMETER
            self.ball_vel[1] = -self.ball_vel[1]
        elif self.ball.top > self.paddle.top:
            self.max_lives -= 1
            if self.max_lives > 0:
                self.state = STATE_BALL_IN_PADDLE
            else:
                self.state = STATE_GAME_OVER

    def show_stats(self):
        if self.font:
            font_surface = self.font.render("SCORED: " + str(self.score), True, GREEN)
            self.screen.blit(font_surface, (20, 5))

            font_surface = self.font.render("MAX LIVES: " + str(self.max_lives), True, ORANGE)
            self.screen.blit(font_surface, (150, 5))

            font_surface = self.font.render("Paddle Width Enlarge", True, VIOLET)
            self.screen.blit(font_surface, (350, 5))

    def show_message(self, message):
        if self.font:
            size = self.font.size(message)
            font_surface = self.font.render(message, True, GREEN)
            x = (SCREEN_SIZE[0] - size[0]) / 2
            y = (SCREEN_SIZE[1] - size[1]) / 2
            self.screen.blit(font_surface, (x, y))

    def start_game(self):
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.clock.tick(60)
            self.screen.fill(WHITE)
            self.get_input()

            if self.state == STATE_PLAYING:
                self.move_ball()
                self.handle_collisions()
            elif self.state == STATE_BALL_IN_PADDLE:
                self.ball.left = self.paddle.left + self.paddle.width / 2
                self.ball.top = self.paddle.top - self.ball.height
                self.show_message("PRESS SPACE KEY to Throw the ball")
            elif self.state == STATE_GAME_OVER:
                self.show_message("GAME OVER. PRESS ENTER KEY to PLAY AGAIN")
            elif self.state == STATE_WON:
                self.show_message("YOU've WON! PRESS ENTER KEY to PLAY AGAIN")

            self.draw_bricks()

            # Drawing paddle
            if not self.enlarge_paddle:
                pygame.draw.rect(self.screen, PADDLE_COLOR, self.paddle)
            elif self.enlarge_paddle:
                self.paddle = pygame.Rect(self.paddle.x, self.paddle.y, 200, PADDLE_HEIGHT)
                pygame.draw.rect(self.screen, PADDLE_COLOR, self.paddle)

            # Drawing ball
            pygame.draw.circle(self.screen, BALL_COLOR,
                               (self.ball.left + BALL_RADIUS, self.ball.top + BALL_RADIUS),
                               BALL_RADIUS)

            self.show_stats()

            pygame.display.flip()


class GameIntro(object):
    def __init__(self):
        pygame.init()

        self.done = False
        screen_width = 700
        screen_height = 400
        self.screen = pygame.display.set_mode([screen_width, screen_height])

        pygame.display.set_caption("Welcome to Brick Breaker Game")

        self.clock = pygame.time.Clock()

        if pygame.font:
            self.font = pygame.font.SysFont('Calibri', 20, True, True)
        else:
            self.font = None

        self.startup_screen()

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            initialize_brick_game()

        if keys[pygame.K_ESCAPE]:
            self.done = True

    def startup_screen(self):
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

            self.clock.tick(60)
            self.screen.fill(WHITE)
            self.get_input()

            font = pygame.font.SysFont('Calibri', 20, False, False)
            message = "Game: Bricks vs Defender - MVP-1 " \
                      "\nAuthor: Vivek Vellaiyappan Surulimuthu" \
                      "\nContact: vivekvellaiyappans@gmail.com" \
                      "\nVersion: v1.0" \
                      "\nDescription:" \
                      "\n  As of now, paddle is used to navigate the ball to break bricks" \
                      "\n  Further improvements will be made over time " \
                      "\n    to complete the " \
                      "\n    Bricks vs Defender Game Scope" \
                      "\nPlay Instructions:" \
                      "\n  Paddle Movement Key Press:" \
                      "\n    Left Arrow Key: move left" \
                      "\n    Right Arrow Key: move right " \
                      "\n\n\nPRESS ENTER TO START PLAY" \
                      "\n\nPRESS ESCAPE KEY TO QUIT GAME"

            screen_text_x = 20
            screen_text_y = 20

            for line in message.splitlines():
                text = font.render(line, True, GREEN)
                self.screen.blit(text, [screen_text_x, screen_text_y])
                screen_text_y += 20

            pygame.display.flip()
            self.clock.tick(60)


def initialize_brick_game():
    brick_breaker_obj = BrickBreaker()
    brick_breaker_obj.start_game()


if __name__ == "__main__":
    game_intro_obj = GameIntro()
    game_intro_obj.startup_screen()
