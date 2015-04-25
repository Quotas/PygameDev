import sys, pygame
from pygame.locals import *
from gen.Render import *


pygame.init()

def main():

    scene = Render()
    while True:
        # Check for user events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


main()