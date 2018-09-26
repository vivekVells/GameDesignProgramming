"""
 Show how to use a sprite backed by a graphic.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
 lab from: http://programarcadegames.com/index.php?chapter=lab_classes_and_graphics&lang=en
"""

import pygame
import random

# Defined colors
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)


# defining Rectangle class
class Rectangle:
    def __init__(self):
        # store object's initial position
        self.x = random.randint(0,700)
        self.y = random.randint(0,500)

        # change object's position
        self.change_y = 10
        self.change_x = 10

        # set the color attrib
        self.color = RED

        # set height and width
        self.height = 10
        self.side_len = 10

    # draw rectangle method
    def draw(self):
        pygame.draw.rect(screen, self.color,
            [self.x, self.y, self.side_len, self.height])

    # moving the object
    def move(self):
        self.x += self.change_x
        self.y += self.change_y


# defining Ellipse class
class Ellipse(Rectangle):
    def __init__(self):
        super().__init__()

    # draw ellipse method
    def draw(self):
        pygame.draw.ellipse(screen, self.color,
            [self.x, self.y, self.side_len, self.height])


# initialize pygame
pygame.init()

# Setting the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Vivek's Graphics Game Tryout")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

my_list = []


# return random instance
def rand_int(a, b):
    return random.randint(a,b)


for x in range(1000):
    rect_object = Rectangle()
    rect_object.x = rand_int(0, 700)
    rect_object.y = rand_int(0, 500)
    rect_object.side_len = rand_int(20, 70)
    rect_object.height = rand_int(20, 70)
    rect_object.change_x = random.randint(-3, 3)
    rect_object.change_y = random.randint(-3, 3)
    rect_object.color = (rand_int(0,255),rand_int(0,255), rand_int(0,255))
    my_list.append(rect_object)

for y in range(1000):
    ellipse_object = Ellipse()
    ellipse_object = Ellipse()
    ellipse_object.x = rand_int(0, 700)
    ellipse_object.y = rand_int(0, 500)
    ellipse_object.side_len = rand_int(20, 70)
    ellipse_object.height = rand_int(20, 70)
    ellipse_object.change_x = random.randint(-3, 3)
    ellipse_object.change_y = random.randint(-3, 3)
    ellipse_object.color = (rand_int(0,255),rand_int(0,255), rand_int(0,255))
    my_list.append(ellipse_object)


# rectangle object creation
# my_object = Rectangle()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    # --- Game logic should go here

    # --- Drawing code should go here


    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    for obj in my_list:
        obj.draw()
        obj.move()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()

