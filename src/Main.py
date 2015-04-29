from src.gen.Render import *
import pygame
import time
import sys


scene = Render()
clock = pygame.time.Clock()

pygame.init()

def main():
    current_time = time.clock()
    frames = 0
    time_delta = 0

    while True:
        keys = pygame.key.get_pressed()
        previous_time, current_time = current_time, time.clock()
        time_delta += (current_time - previous_time)
        scene.clear()
        frames += 1
        clock.tick(60)

        if keys[pygame.K_r]:
            scene.pixel_data_buffer.randomise_tiles()
            scene.pixel_data_buffer.create_tile_map()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if time_delta >= 1:
            time_delta -= 1
            pygame.display.set_caption("fps:" + str(frames))
            frames = 0
        scene.render()

main()