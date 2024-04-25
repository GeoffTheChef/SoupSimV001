import sys
import pygame
from pygame.locals import *
from soup_pot import SOUP_POT

# Initialize Pygame
pygame.init()

# Set up the display
GAME_WINDOW = pygame.display.set_mode((500, 500))

# Create a SOUP_POT object
soup_pot_one = SOUP_POT(GAME_WINDOW)

# Main game loop
while True:
    GAME_WINDOW.fill(pygame.Color("White"))
    soup_pot_one.draw()

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            soup_pot_one.update(mouse_pos)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
