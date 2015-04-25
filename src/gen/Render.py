import pygame
from GenLevel import GenLevel

# Constants
TILE_SIZE = 100
NUM_OF_ROWS = 5
NUM_OF_COLUMNS = 5
MAP_WIDTH = TILE_SIZE * NUM_OF_COLUMNS
MAP_HEIGHT = TILE_SIZE * NUM_OF_ROWS


class Render(object):
    def __init__(self):
        self.Level = GenLevel(5, 5, 5)
        self.game_window = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))
        self.render()

        print "Initializing Render object: ", (self.Level.level[3][3].neighbours)

    def render(self):
        start_room = self.Level.level[3][3].neighbours
        for row in range(MAP_HEIGHT):
            for column in range(MAP_WIDTH):

                # Draw the rooms
                pygame.draw.rect(self.game_window, (200, 200, 200),
                                 (column * TILE_SIZE, row * TILE_SIZE,
                                  TILE_SIZE, TILE_SIZE), 25)

        # Draw paths
        for i in range(len(start_room)):
            def draw_path():
                if start_room[i] == 1:
                    print("Connection drawn")
                    if i == 0:
                        pygame.draw.rect(self.game_window, (222, 23, 23),
                                         (TILE_SIZE * 2 + TILE_SIZE/2, TILE_SIZE * 2,
                                         TILE_SIZE / 10, TILE_SIZE / 10))
                    elif i == 1:
                        pygame.draw.rect(self.game_window, (222, 23, 23),
                                         (TILE_SIZE * 3, TILE_SIZE * 2 + TILE_SIZE * .5,
                                         TILE_SIZE / 10, TILE_SIZE / 10))
                    elif i == 2:
                        pygame.draw.rect(self.game_window, (222, 23, 23),
                                         (TILE_SIZE * 2 + TILE_SIZE/2, TILE_SIZE * 3,
                                         TILE_SIZE / 10, TILE_SIZE / 10))
                    elif i == 3:
                        pygame.draw.rect(self.game_window, (222, 23, 23),
                                         (TILE_SIZE * 2, TILE_SIZE * 2 + TILE_SIZE * .5,
                                         TILE_SIZE / 10, TILE_SIZE / 10))

                else:
                    print("No Connection")

            draw_path()


