import numpy as np
import random

from src.gen.SpriteSheet import SpriteSheet


class Screen(object):
    def __init__(self, width, height):
        self.sprite_sheet = SpriteSheet()
        self.width = width
        self.height = height
        self.pixels = np.zeros((width, height)).astype(np.uint32)
        self.tile_map = [0 for x in range(64*64)]

        for y in range(0, 64):
            for x in range(0, 64):
                self.tile_map[x + y * 64] = random.randrange(0, 3)

        for y in range(0, 64):
            for x in range(0, 64):
                if self.tile_map[x + y * 64] == 0:
                    self.tile_map[x + y * 64] = self.sprite_sheet.GRASS_TILE00.astype(np.uint32)
                elif self.tile_map[x + y * 64] == 1:
                    self.tile_map[x + y * 64] = self.sprite_sheet.GRASS_TILE01.astype(np.uint32)
                elif self.tile_map[x + y * 64] == 2:
                    self.tile_map[x + y * 64] = self.sprite_sheet.GRASS_TILE02.astype(np.uint32)
                else:
                    self.tile_map[x + y * 64] = self.sprite_sheet.GRASS_TILE03.astype(np.uint32)


    def create_tile_map(self):
        for y in range(0, self.height):
            yy = y
            for x in range(0, self.width):
                xx = x
                tileIndex = ((xx >> 5) & 63) + ((yy >> 5) & 63) * 64
                self.pixels[x, y] = self.tile_map[tileIndex][(x & 31) + (y & 31) * 32].astype(np.uint32)

    def render_tile(self, tile):
        for y in range(0, len(tile)):
            for x in range(0, len(tile)):
                self.pixels[x, y] = tile.pixels[x, y]

    def update_tile_map(self, offsetX, offsetY):
        pass

    def clear(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                self.pixels[x, y] = 0
