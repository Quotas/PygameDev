import pygame
import random
from Room import Room

pygame.init()


class GenLevel(object):
    counter = 0

    def __init__(self, map_width, map_height, depth):
        self.map_height = map_height
        self.map_width = map_width
        self.depth = depth
        self.level = []
        self.create_rooms()

    #generates levels and relationships
    def create_rooms(self):
        self.level = [[Room([random.randint(0, 1) for i in range(0, 4)])
                       for x in range(self.map_width)] for y in range(self.map_height)]