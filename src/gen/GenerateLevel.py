import pygame
from random import randrange
pygame.init()

class GenerateLevel(object):
    
    room_width_min = 5
    room_width_max = 15
    room_height_min = 10
    room_height_max = 25
    
    def __init__(self,height, width, room_count):
        self.height = height
        self.width = width
        self.level_layout = None
        self.room_count = room_count
        self.level_generated = False
        self.neighbour_nodes = None
        self.genRectArray()
        self.getNeighbourNodes()
        self.levelCorrections()
    
    def levelCorrections(self):
        for i in range(0, len(self.level_layout) -1):
            if i > (len(self.level_layout) - 2):
                break
            else:
                self.stopOverlap(self.level_layout[i], self.level_layout[i + 1])
        
        
    def genRectArray(self):    
        while (self.level_generated != True):
            for i in self.room_count:
                self.level_layout.add(pygame.rect(randrange(0, self.height), randrange(0, self.width), randrange(GenerateLevel.room_height_min, GenerateLevel.room_height_max), randrange(GenerateLevel.room_width_min, GenerateLevel.room_width_max)))
        return False

    def newNeighbourNode(self, node_a, node_b):
        self.neighbour_nodes.add((node_a, node_b))
        
    def stopOverlap(self, node_a, node_b):
        for i in range(node_a.x, node_a.width):
            if node_b.x == i:
                if node_b.x > self.height / 2:
                    node_b.x += (node_b.x - node_a.x) + 1 
                else:
                    node_b.x -= (node_a.x - node_b.x) + 1
            for j in range(0, node_a.y + node_a.height):
                if node_b.y == j:
                    if node_b.y > self.width / 2:
                        node_b.y += (node_b.y - node_a) + 1
                    else:
                        node_b.y -= (node_a.y - node_b.y) + 1
     
                
            
    def getNeighbourNodes(self):
        for i in range(0, len(self.level_layout) - 1):
            if i + 1 < len(self.level_layout):
                node_a = self.level_layout[i]
                node_b = self.level_layout[i + 1]
                node_c = self.level_layout[i + 2]
                if (node_a.x - node_b.x) > (node_b.x - node_c.x):
                    self.newNeighbourNode(node_b, node_c)
                else:
                    self.newNeighbourNode(node_a, node_b)
            else:
                continue
                    
