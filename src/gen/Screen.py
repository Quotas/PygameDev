import pygame
from random import randrange
import numpy as np


class Screen(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = np.zeros((width, height)).astype(np.uint32)
        self.tiles = np.random.randint(0, 255 ** 3, 64 * 64)


    def create_tile_map(self):
        for y in range(0, self.height):
            yy = y
            for x in range(0, self.width):
                xx = x
                tileIndex = ((xx >> 4) & 63) + ((yy >> 4) & 63) * 64
                self.image[x, y] = self.tiles[tileIndex]

    def update_tile_map(self, offsetX, offsetY):
        pass

    def clear(self):
        pixels = pygame.PixelArray(self.image)
        for i in range(0, len(pixels)):
            pixels[i] = 0
        self.image = pixels.make_surface()