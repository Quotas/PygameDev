import numpy as np
import random
import pygame

from src.gen.SpriteSheet import SpriteSheet


class Screen(object):
    def __init__(self, width, height):
        self.sprite_sheet = SpriteSheet()
        self.width = width
        self.height = height
        self.pixels = np.zeros((width, height)).astype(np.uint32)
        self.tile_map_width = 64
        self.tile_map_height = 64
        self.tile_map = [0 for x in range(64 * 64)]
        self.randomise_tiles()

    def create_tile_map(self):
        for y in range(0, self.height):
            yy = y
            for x in range(0, self.width):
                xx = x
                tileIndex = ((xx >> 5) & (64 - 1)) + ((yy >> 5) & (64 - 1)) * 64
                self.pixels[x, y] = self.tile_map[tileIndex][(x & 31) + (y & 31) * 32].astype(np.uint32)

    def randomise_tiles(self):
        for y in range(0, 64):
            for x in range(0, 64):
                self.tile_map[x + y * 64] = random.randrange(0, 3)

        for y in range(0, self.tile_map_height):
            for x in range(0, self.tile_map_width):
                if self.tile_map[x + y * self.tile_map_width] == 0:
                    self.tile_map[x + y * self.tile_map_width] = self.sprite_sheet.GRASS_TILE00
                elif self.tile_map[x + y * self.tile_map_width] == 1:
                    self.tile_map[x + y * self.tile_map_width] = self.sprite_sheet.GRASS_TILE01
                elif self.tile_map[x + y * self.tile_map_width] == 2:
                    self.tile_map[x + y * self.tile_map_width] = self.sprite_sheet.BUSH_TILE00
                elif self.tile_map[x + y * self.tile_map_width] == 5:
                    self.tile_map[x + y * self.tile_map_width] = self.sprite_sheet.LAVA_TILE00

    def update_tile_map(self, offsetX, offsetY):
        pass

    def clear(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                self.pixels[x, y] = 0
