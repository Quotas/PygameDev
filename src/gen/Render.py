import pygame
from src.gen.GenLevel import GenLevel

pygame.init()
from src.gen.GenerateLevel import *


class Render(object):
    def __init__(self):
        self.Level = GenLevel(60, 85, 30, 800, 600)
        self.game_window = pygame.display.set_mode((600, 800))
        self.white = pygame.Color(255, 255, 255, 0)
        self.Level.create_rooms()

    def render(self):
        for i in range(0, len(self.Level.level_layout)):
            self.game_window.fill(self.white, self.Level.level_layout[i])
        pygame.display.flip()
