from src.gen.Render import *
import pygame
import time
scene = Render()
clock = pygame.time.Clock()

pygame.init()



def main():
    current_time = time.clock()
    frames = 0
    time_delta = 0

    while True:
        previous_time, current_time = current_time, time.clock()
        time_delta += (current_time - previous_time)
        scene.render()
        frames += 1
        if time_delta >= 1:
            time_delta -= 1
            pygame.display.set_caption("fps:" + str(frames))
            frames = 0


main()