from config import GRID_SIZE, NUM_LEVELS

class Level:

    def __init__(self, main_clr = (255, 255, 255), supp_clr = (200, 200, 200)):
        self.grid = [[None for _ in range(GRID_SIZE[0])] for _ in range(GRID_SIZE[1])]
        self.main_clr = main_clr
        self.supp_clr = supp_clr
        self.walls = []

    def add_walls(self, *args):
        for wall in args:
            self.walls.append(wall)
#

levels = [Level() for _ in range(NUM_LEVELS)]

levels[0] = Level()
