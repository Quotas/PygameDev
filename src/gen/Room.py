TOP = 0
RIGHT = 1
BOTTOM = 2
LEFT = 3

class Room(object):


    def __init__(self, neighbours):
        # neighbours is list of connected rooms [top, right, bottom, left]
        # 1 - connected
        # 0 - not connected
        self.neighbours = neighbours
        self.ROOM_CONNECTIONS = {
            TOP: neighbours[0],
            RIGHT: neighbours[1],
            BOTTOM: neighbours[2],
            LEFT: neighbours[3]
        }