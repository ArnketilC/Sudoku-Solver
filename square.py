"""Square/Button for my sudoku solver."""

import pygame

class Square():
    """Square that will contain value for my sudoku."""

    def __init__(self, settings, screen, value):
        """Construct a basic button."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width = 25
        self.height = 25
        self.color = (255, 20, 20)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

    def draw(self):
        """Draw the button/square."""
        self.screen.fill(self.color, self.rect)