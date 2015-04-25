class genRooms(object):

    def __init__(self):
        self.width = 27
        self.height = 27
        self.level_map = ["@"] * (27 * 27)
        self.level_map[len(self.level_map)) = 'O'
        self.max_rooms = 13
        
        while counter not self.max_rooms    
            for x in range(0, self.width):
                for y in range(0, self.height):
                    if self.level_map[x + y * self.width] = 'O'
                        render_left = rand.randrange(0, 1)
                        render_right = rand.randrange(0, 1)
                        render_bottom = rand.randrange(0, 1)
                        render_top = rand.randrange(0, 1)
                        if render_top: 
                            self.level_map[x + (y - 1) * self.width] = 'R'
                            counter += 1
                        if render_bottom: 
                            self.level_map[x + (y + 1) * self.width] = 'R'
                            counter += 1
                        if render_right: 
                            self.level_map[(x - 1) + y * self.width] = 'R'
                            counter += 1
                        if render_left: 
                            self.level_map[(x + 1) + y * self.width] = 'R'
                            counter += 1
                    if self.level_map[x + y * self.width] = 'R'
                        render_left = rand.randrange(0, 1)
                        render_right = rand.randrange(0, 1)
                        render_bottom = rand.randrange(0, 1)
                        render_top = rand.randrange(0, 1)
                        if render_top: 
                            self.level_map[x + (y - 1) * self.width] = 'R'
                            counter += 1
                        if render_bottom: 
                            self.level_map[x + (y + 1) * self.width] = 'R'
                            counter += 1
                        if render_right: 
                            self.level_map[(x - 1) + y * self.width] = 'R'
                            counter += 1
                        if render_left: 
                            self.level_map[(x + 1) + y * self.width] = 'R'
                            counter += 1
                            
            def printRooms(self):
                for y in self.height:
                    for x in self.width:
                        print str(self.level_map[x + y])