import pygame


class SpriteSheet(object):


    def __init__(self, file):
        self.file_name = file
        self.sprites = pygame.sprite.group()


    def create_sprite(self, x, y, size):
        pass