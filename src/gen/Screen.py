import pygame
from random import randrange


class Screen(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = pygame.Surface((width, height))
        self.tiles = [None] * (64 * 64)

        for i in range(0, len(self.tiles)):
            self.tiles[i] = randrange(0, int("0xffffff", 16))


    def render(self):
        pixels = pygame.PixelArray(self.image)
        for y in range(0, self.height):
            yy = y
            for x in range(0, self.width):
                xx = x
                tileIndex = ((xx >> 3) & 63) + ((yy >> 3) & 63) * 64
                pixels[x, y] = self.tiles[tileIndex]
        self.image = pixels.make_surface()


    def clear(self):
        pixels = pygame.PixelArray(self.image)
        for i in range(0, len(pixels)):
            pixels[i] = 0
        self.image = pixels.make_surface()