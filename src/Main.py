from src.gen.Render import *

scene = Render()
clock = pygame.time.Clock()


def main():
    pygame.init()
    while True:
        scene.render()
        pygame.display.update()
        clock.tick(500)
        print("fps:", clock.get_fps())


main()