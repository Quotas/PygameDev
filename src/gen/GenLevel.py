import pygame
import random
from Room import Room

pygame.init()


class GenLevel(object):
    def __init__(self, map_width, map_height, depth):
        self.map_height = map_height
        self.map_width = map_width
        self.depth = depth
        self.level = []
        self.create_rooms()
        self.add_neighbours()

    def create_rooms(self):
        self.level = [[(Room([0, 0, 0, 0])) for x in range(self.map_width)] for y in range(self.map_height)]
        room_thing = self.level[25][15]

        # Level attributes
        print "Level x: ", len(self.level[0])
        print "Level y: ", len(self.level)
        print "Room properties: ", room_thing.neighbours

    def add_neighbours(self):
        start_room = self.level[25][15]
        for neighbour in range(len(start_room.neighbours)):
            start_room.neighbours[neighbour] = random.randint(0, 1)
        print "Start room neighbours: ", start_room.neighbours