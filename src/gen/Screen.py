import pygame
from random import randrange
import numpy as np
from src.gen.SpriteSheet import SpriteSheet


class Screen(object):
    def __init__(self, width, height):
        self.sprite_sheet = SpriteSheet()
        self.width = width
        self.height = height
        self.pixels = np.zeros((width, height)).astype(np.uint32)

    def create_tile_map(self):
        for y in range(0, self.height):
            yy = y
            for x in range(0, self.width):
                xx = x
                #tileIndex = ((xx >> 4) & 63) + ((yy >> 4) & 63) * 64
                self.pixels[x, y] = self.sprite_sheet.GRASS_TILE00[(x & 31) + (y & 31) * 32]

    def update_tile_map(self, offsetX, offsetY):
        pass

    def clear(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                self.pixels[x, y] = 0
