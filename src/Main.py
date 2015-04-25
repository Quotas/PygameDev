import sys, pygame
from pygame.locals import *
from gen.Render import *


pygame.init()
clock = pygame.time.Clock()

def main():

    scene = Render()
    while True:
        # Check for user events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(60)
        pygame.display.update()


main()