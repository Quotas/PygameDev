from gen.Render import *

scene = Render()
pygame.init()

def main():

    while True:
        scene.render()
        pygame.display.update()


main()