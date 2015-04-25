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
        self.add_neighbours()

    def create_rooms(self):
        self.level = [[Room([0, 0, 0, 0]) for x in range(self.map_width)] for y in range(self.map_height)]

        # Level attributes
        print "Level x: ", len(self.level[0])
        print "Level y: ", len(self.level)

    def add_neighbours(self):

        self.level = [[[random.randint(0, 1) for neighbour in self.level[x][y].neighbours] for x in range(self.map_width)] for y in range(self.map_height)]

        # Create connections for the center room
        """
        start_room = self.level[3][3]
        self.counter += 1
        print self.counter
        for neighbour in range(len(start_room.neighbours)):
            start_room.neighbours[neighbour] = random.randint(0, 1)
        """

