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
        self.tile_map = np.zeros(64*64, dtype=object)
        self.randomise_tiles()

    def create_tile_map(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                tileIndex= ((x >> 5) & (64 - 1)) + ((y >> 5) & (64 - 1)) * 64
                self.pixels[x, y] = self.tile_map[tileIndex][(x & 31) + (y & 31) * 32].astype(np.uint32)

    def randomise_tiles(self):
        for y in range(0, 64):
            for x in range(0, 64):
                self.tile_map[x + y * 64] = 0
                if self.tile_map[x+ y * 64] == 0:
                    self.tile_map[x + y * 64] = self.sprite_sheet.GRASS_TILE00.astype(np.uint32)
                elif self.tile_map[x + y * 64] == 1:
                    self.tile_map[x + y * 64] = self.sprite_sheet.GRASS_TILE01.astype(np.uint32)
                elif self.tile_map[x + y * 64] == 2:
                    self.tile_map[x + y * 64] = self.sprite_sheet.BUSH_TILE00.astype(np.uint32)
                elif self.tile_map[x + y * 64] == 5:
                    self.tile_map[x + y * 64] = self.sprite_sheet.LAVA_TILE00.astype(np.uint32)


    def update_tile_map(self, offsetX, offsetY):
        pass

    def clear(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                self.pixels[x, y] = 0
