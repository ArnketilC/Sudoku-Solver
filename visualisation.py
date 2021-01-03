"""Sudoku game."""
import pygame
import json
import sys
from os import path
from pygame.constants import QUIT
from square import Square

with open(path.join(sys.path[0], 'settings.json'), 'r') as json_file:
    SETTINGS = json.load(json_file)

def check_event():
    """Event hangler."""
    for even in pygame.event.get():
        if even.type == QUIT:
            sys.exit()


def draw_grid(button):
    """Draw the sudoku grid."""
    blockSize = (SETTINGS['resolution'][1]-50)/9
    for x in range(9):
        for y in range(9):
            rect = pygame.Rect(10 + x*blockSize, 10 + y*blockSize,
                               blockSize, blockSize)
            pygame.draw.rect(SCREEN, SETTINGS['white'], rect, 1)
    button.draw()


def run():
    """Run main loop."""
    global SCREEN
    pygame.init()
    SCREEN = pygame.display.set_mode(tuple(SETTINGS['resolution']))
    SCREEN.fill(SETTINGS['blue'])
    pygame.display.set_caption("My sudoku Solver/Game")
    icon = pygame.image.load(path.join(sys.path[0], "resources/sudoku.png"))
    pygame.display.set_icon(icon)

    button = Square(SETTINGS, SCREEN, 5)
    draw_grid(button)

    while True:
        check_event()
        pygame.display.update()


if __name__ == '__main__':
    #Run this part only on launch.
    run()