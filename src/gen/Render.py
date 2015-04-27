import pygame
from src.gen.GenLevel import GenLevel
from src.gen.Screen import Screen
from src.gen.GenerateLevel import *


class Render(object):
    def __init__(self):
        self.Level = GenLevel(60, 85, 20, 800, 600)
        self.pixel_data_buffer = Screen(800, 800)
        self.game_window = pygame.display.set_mode((800, 800))
        self.pixel_data_buffer.create_tile_map()

    def render(self):
        pygame.surfarray.blit_array(self.game_window, self.pixel_data_buffer.pixels)
        pygame.display.update()

    def clear(self):
        self.game_window.fill(pygame.Color(0, 0, 0))