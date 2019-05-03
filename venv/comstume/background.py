import pygame
from pygame.locals import *

class background:
    # set all class variables in the constructor
    def __init__(self, newX, newY):
        self.x = 0
        self.y = 0
        self.img = pygame.image.load("BACKROUND_1.gif")

        # draw your image
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))