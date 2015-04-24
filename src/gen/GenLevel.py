import pygame
from random import randrange
from Room import Room

pygame.init()


class GenLevel(object):
    def __init__(self, map_height, map_width):
        self.map_height = map_height
        self.map_width = map_width
        self.rooms = []
        self.neighbour_nodes = []
        self.create_rooms()

    def create_rooms(self):
        level = [(Room(x, y, [0, 0, 0, 0])) for y in range(self.map_height) for x in range(self.map_width)]
        room_thing = level[0]
        print len(level)
        print(room_thing.x, room_thing.y, room_thing.neighbours)
