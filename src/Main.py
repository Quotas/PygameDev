from gen.Render import *
import pygame
scene = Render()
clock = pygame.time.Clock()

pygame.init()

def main():

    while True:
        scene.render()
        pygame.display.update()
        clock.tick(500)
        print("fps:", clock.get_fps())


main()