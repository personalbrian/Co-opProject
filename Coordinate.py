

class Coordinate:
    def __init__(self):
        self.rows = None
        self.columns = None
        self.hitSpace = False
        self.boat_on = False

    def boat_hit(self):
        self.hitSpace = True

    def set_rows(self, string):
        self.rows = string.upper()

    def set_columns(self, ints):
        self.columns = ints

    def boat_true(self):
        self.boat_on = True
