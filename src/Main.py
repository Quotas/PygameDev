from gen.Render import *

scene = Render()

def main():
    
    while True:
        scene.renderLevel()
        scene.flip()
        
        