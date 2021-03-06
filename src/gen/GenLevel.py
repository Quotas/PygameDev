import pygame
from random import randrange
from src.gen.Room import Room
pygame.init()


class GenLevel(object):

    def __init__(self, ROOM_MIN_SIZE, ROOM_MAX_SIZE, MAX_ROOMS, MAP_HEIGHT, MAP_WIDTH):
        self.room_min_size = ROOM_MIN_SIZE
        self.room_max_size = ROOM_MAX_SIZE
        self.max_rooms = MAX_ROOMS
        self.map_height = MAP_HEIGHT
        self.map_width = MAP_WIDTH
        self.rooms = []
        self.level_layout = []
        self.neighbour_nodes = []
        self.create_rooms()
        self.getNeighbourNodes()

    def create_rooms(self):
        for r in range(0, self.max_rooms):
            w = randrange(self.room_min_size, self.room_max_size)
            h = randrange(self.room_min_size, self.room_max_size)
            x = randrange(0, self.map_width - w - 1)
            y = randrange(0, self.map_height - h - 1)
            new_room = Room(x, y, w, h)
            failed = False
            for other_room in self.rooms:
                if new_room.intersect(other_room):
                    failed = True
                    break

            if not failed:
                self.level_layout.append(pygame.Rect(x, y, w, h))
            self.rooms.append(new_room)

    def newNeighbourNode(self, node_a, node_b):
        self.neighbour_nodes.append(node_a)
        self.neighbour_nodes.append(node_b)

    def getNeighbourNodes(self):
        for i in range(0, len(self.level_layout)):
            if i + 2 < len(self.level_layout):
                node_a = self.level_layout[i]
                node_b = self.level_layout[i + 1]
                node_c = self.level_layout[i + 2]
                if (node_a.x - node_b.x) > (node_b.x - node_c.x):
                    self.newNeighbourNode(node_b, node_c)
                else:
                    self.newNeighbourNode(node_a, node_b)
            else:
                break


