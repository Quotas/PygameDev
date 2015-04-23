import pygame
from random import randrange

pygame.init()


class GenerateLevel(object):
    def __init__(self, height, width, room_count):
        self.height = height
        self.width = width
        self.level_layout = []
        self.room_count = room_count
        self.level_generated = False
        self.neighbour_nodes = []
        self.room_width_min = 75
        self.room_width_max = 175
        self.room_height_min = 50
        self.room_height_max = 125
        self.finished_overlap_corrections = False
        self.gen_rect_array()
        self.getNeighbourNodes()
        self.level_corrections()

    def level_corrections(self):
        for i in range(0, len(self.level_layout) - 1):
            self.stopOverlap()

    def gen_rect_array(self):
        for i in range(0, self.room_count):
            if len(self.level_layout) == 0:
                self.level_layout.append(pygame.Rect(randrange(0, 400), randrange(0, 400),
                                                 randrange(self.room_height_min, self.room_height_max),
                                                 randrange(self.room_width_min, self.room_width_max)))
            else:
                self.level_layout.append(pygame.Rect(self.level_layout[i].x + self.level_layout[i].height + 2, self.level_layout[i].y + self.level_layout[i].width + 2, randrange(self.room_height_min, self.room_height_max),
                                                 randrange(self.room_width_min, self.room_width_max)))

    def newNeighbourNode(self, node_a, node_b):
        self.neighbour_nodes.append((node_a, node_b))

    def stopOverlap(self):
        for i in range(len(self.level_layout)):
            for j in range(len(self.level_layout)):
                if (self.level_layout[i].x == self.level_layout[j].x + self.level_layout[j].width) or (self.level_layout[i].x == self.level_layout[j].x + self.level_layout[j].height):
                    if self.level_layout[i].x > self.level_layout[j].x:
                        self.level_layout[i].y += (self.level_layout[i].y - self.level_layout[j].y) - self.level_layout[j].height + 2
                    else:
                        self.level_layout[i].y -= (self.level_layout[i].y + self.level_layout[j].y) - self.level_layout[j].height + 2



    def getNeighbourNodes(self):
        for i in range(0, len(self.level_layout) - 1):
            if i + 2 < len(self.level_layout):
                node_a = self.level_layout[i]
                node_b = self.level_layout[i + 1]
                node_c = self.level_layout[i + 2]
                if (node_a.x - node_b.x) > (node_b.x - node_c.x):
                    self.newNeighbourNode(node_b, node_c)
                else:
                    self.newNeighbourNode(node_a, node_b)
            else:
                continue
