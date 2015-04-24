
class Room(object):
    def __init__(self, neighbours):
        # neighbours is list of connected rooms [top, right, bottom, left]
        # 1 - connected
        # 0 - not connected
        self.neighbours = neighbours