# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
 
import pygame
import math
 
# Define some colors
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)
BLUE = (7, 15, 255)
LIGHT_GRAY = (211,211,211)

def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, WHITE, [1 + x, y, 10, 10], 0)
 
    # Legs
    pygame.draw.line(screen, WHITE, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, WHITE, [5 + x, 17 + y], [x, 27 + y], 2)
 
    # Body
    pygame.draw.line(screen, GREEN, [5 + x, 17 + y], [5 + x, 7 + y], 2)
 
    # Arms
    pygame.draw.line(screen, BLUE, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, BLUE, [5 + x, 7 + y], [1 + x, 17 + y], 2)
    
# Setup
pygame.init()
  
# Set the width and height of the screen [width,height]
size = [700, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Chase IT game by Vivek!")
 
#Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Hide the mouse cursor
pygame.mouse.set_visible(1)

x_stick = x_mouse = 10
y_stick = y_mouse = 10
X_SPEED = 3
Y_SPEED = 3

font = pygame.font.SysFont('Calibri', 25, True, False)
found_mouse = font.render("Stick found mouse", True, WHITE)
not_started = font.render("Press any key to reach mouse!", True, WHITE)
find_mouse = font.render("Hey Stick! I am here!", True, WHITE)

caught = False
goto_initial_position = True

# -------- Main Program Loop -----------
while not done:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

        elif event.type == pygame.KEYDOWN:
            goto_initial_position = False
            if caught and event.type == pygame.KEYDOWN:
                    x_stick = y_stick = 10
                    caught = False
                    goto_initial_position = True


    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

    # initial state of the mouse in location 10,10


    if goto_initial_position:
        screen.fill(BLACK)
        draw_stick_figure(screen, 10, 10)
        screen.blit(not_started, [25, 15])
        pos = pygame.mouse.get_pos()
        screen.blit(find_mouse, [(pos[0] + 15), pos[1]])

    # only if key press done, then start stick to move to find mouse pointer
    if not goto_initial_position:
        stick_to_mouse_x = (x_mouse - x_stick)
        stick_to_mouse_y = (y_mouse - y_stick)

        theta = math.atan2(stick_to_mouse_x, stick_to_mouse_y)

        # in one frame, stick travels
        dx = X_SPEED * math.sin(theta)
        dy = Y_SPEED * math.cos(theta)

        x_stick += dx
        y_stick += dy

        # to avoid the jittering effect when the stick meets mouse
        # there are chances when stick would cross the mouse and come back
        if(abs(x_stick - x_mouse) <= X_SPEED):
            x_stick = x_mouse


        if(abs(y_stick - y_mouse) <= Y_SPEED):
            y_stick = y_mouse

        # Call draw stick figure function
        pos = pygame.mouse.get_pos()
        x_mouse = pos[0]
        y_mouse = pos[1]

        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(BLACK)

        draw_stick_figure(screen, x_stick, y_stick)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # text
        if(x_stick == x_mouse) and y_stick == y_mouse:
            caught = True
            screen.blit(found_mouse, [x_stick + 15, y_stick + 10])

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 20 frames per second
    clock.tick(60)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()