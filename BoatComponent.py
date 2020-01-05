import Player

movement_board_up = {
    "B": "A",
    "C": "B",
    "D": "C",
    "E": "D",
    "F": "E",
    "G": "F",
    "H": "G",
    "I": "H",
    "J": "I",
}

movement_board_down = {
    "A": "B",
    "B": "C",
    "C": "D",
    "D": "E",
    "E": "F",
    "F": "G",
    "G": "H",
    "H": "I",
    "I": "J",
}


class AlreadyHitException(Exception):
    def __init__(self):
        pass


class BoatComponent:
    def __init__(self, string, number):
        self.y_coordinate = string
        self.x_coordinate = number
        self.boat_been_hit = False

    def confirm_boat_placement(self, coordinate):
        dummy_rows = coordinate.rows
        dummy_column = coordinate.columns
        if self.y_coordinate == dummy_rows and self.x_coordinate == dummy_column:
            coordinate.boat_placed()

    def hit(self, player):
        if self.boat_been_hit:
            raise AlreadyHitException
        self.boat_been_hit = True
        player.update()

    def set_y(self, string):
        self.y_coordinate = string

    def set_x(self, number):
        self.x_coordinate = number

    def move_singular_right_up(self):
        self.x_coordinate += 1
        new_space = movement_board_up.get(self.y_coordinate, None)
        self.y_coordinate = new_space

    def move_singular_down_left(self):
        new_space = movement_board_down.get(self.y_coordinate, None)
        self.y_coordinate = new_space
        self.x_coordinate = self.x_coordinate - 1
