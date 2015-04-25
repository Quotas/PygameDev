import pygame
from GenLevel import GenLevel
from Screen import Screen
from GenerateLevel import *
pygame.init()





class Render(object):
    def __init__(self):
        self.Level = GenLevel(60, 85, 20, 800, 600)
        self.pixel_data_buffer = Screen(800, 800)
        self.game_window = pygame.display.set_mode((800, 800))
        self.pixel_data_buffer.create_tile_map()

    def render(self):
        self.surfarray.blit_array(self.game_window, self.pixel_data_buffer.image)

