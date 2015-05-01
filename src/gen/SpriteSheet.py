import pygame
import numpy as np
from src.gen.Screen import *


class SpriteSheet(object):
    def __init__(self):
        self.spritesheet = pygame.image.load(
            "L:/Users/Seamus/Desktop/PygameDev/PygameDev/assets/sprites/spritesheet.png")
        self.sprite_sheet_image_array = pygame.surfarray.array2d(self.spritesheet).astype(np.uint32)
        self.sprites = pygame.sprite.Group()

        self.GRASS_TILE00 = self.create_sprite(0, 0, 32)
        self.GRASS_TILE01 = self.create_sprite(32, 0, 32)
        self.GRASS_TILE02 = self.create_sprite(64, 0, 32)
        self.GRASS_TILE03 = self.create_sprite(0, 32, 32)
        self.STONE_TILE00 = self.create_sprite(96, 0, 32)
        self.LAVA_TILE00 = self.create_sprite(32, 32, 32)
        self.BUSH_TILE00 = self.create_sprite(64, 32, 32)


    def create_sprite(self, posx, posy, size):
        pixels = np.zeros(size * size)
        for x in range(0, size):
            for y in range(0, size):
                pixels[x + y * size] = (self.sprite_sheet_image_array[x + posx][y + posy] & 0x0000FF) << 16 | (
                    self.sprite_sheet_image_array[x + posx][y + posy] & 0x00FF00) | ( self.sprite_sheet_image_array[x + posx][y + posy] & 0xFF0000) >> 16
        return np.array(pixels)

    def render_sprite(self, xOffset, yOffset):
        Screen.render_tile()
