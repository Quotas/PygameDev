import pygame
from GenLevel import GenLevel
from Screen import Screen
from GenerateLevel import *



class Render(object):
    def __init__(self):
        self.Level = GenLevel(60, 85, 20, 800, 600)
        self.pixel_data_buffer = Screen(600, 800)
        self.game_window = pygame.display.set_mode((600, 800))

    def render(self):
        self.pixel_data_buffer.clear()
        self.pixel_data_buffer.render()
        self.game_window.blit(self.pixel_data_buffer.image, (0, 0))

