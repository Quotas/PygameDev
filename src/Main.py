from src.gen.Render import *

scene = Render()


def main():
    pygame.init()
    while True:
        scene.render()


main()