"""
 Show how to use a sprite backed by a graphic.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Vivek's 1st House via PyGame")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

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
    # rect(screen, GREEN, [x,y,breadth, length], 0)
    # polygon(screen, BLACK, [[midx, midy], [leftx, lefty], [rightx, righty]], 5)

    # drawing house
    pygame.draw.rect(screen, RED, [100, 200, 200, 200], 0)

    # drawing chimney
    pygame.draw.rect(screen, BLACK, [125, 140, 20, 60], 0)

    # drawing roof
    pygame.draw.polygon(screen, WHITE, [[200, 100], [100, 200], [300, 200]], 0)
    pygame.draw.polygon(screen, BLACK, [[200, 100], [100, 200], [300, 200]], 3)


    # drawing window
    pygame.draw.rect(screen, GREEN, [125, 250, 10, 30], 0)
    pygame.draw.rect(screen, GREEN, [175, 250, 10, 30], 0)
    pygame.draw.rect(screen, GREEN, [225, 250, 10, 30], 0)
    pygame.draw.rect(screen, GREEN, [275, 250, 10, 30], 0)

    # drawing the door
    pygame.draw.rect(screen, BLACK, [190, 350, 20, 50], 0)


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()

