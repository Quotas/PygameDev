import pygame
pygame.init()
from GenerateLevel import *

class Render(object):

    def __init__(self):
        self.Level = GenerateLevel(600, 800, 15)
        self.game_window = pygame.Surface(600, 800)
        self.white = pygame.Color(255, 255, 255, 0)
        
    def renderLevel(self):
        for i in range(0, len(self.Level.level_layout) - 1):
            self.game_window.fill(self.white, self.Level.level_layout[i])
            #pygame.draw.rect(self.game_window, self.white, self.Level.level_layout[i], 0)
        