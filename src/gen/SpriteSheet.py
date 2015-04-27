import pygame
import numpy as np

class SpriteSheet(object):


    def __init__(self):
        self.spritesheet = pygame.image.load("L:/Users/Seamus/Desktop/PygameDev/PygameDev/assets/sprites/spritesheet.png")
        self.sprite_sheet_image_array = pygame.surfarray.array2d(self.spritesheet)
        self.sprites = pygame.sprite.Group()

        self.GRASS_TILE00 = self.create_sprite(0, 0, 32)
        self.GRASS_TILE01 = self.create_sprite(32, 0, 32)
        self.GRASS_TILE02 = self.create_sprite(64, 0, 32)
        self.STONE_TILE00 = self.create_sprite(96, 0, 32)

    def create_sprite(self, posx, posy, size):
        pixels = np.zeros(size * size)
        for x in range(0, size):
            for y in range(0, size):
                pixels[x + y * size] = self.sprite_sheet_image_array[x + posx, y + posy]
        return pixels