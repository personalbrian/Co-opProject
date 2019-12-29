from BoatComponent import BoatComponent


class OutOfBoardException(Exception):
    def __init__(self):
        pass


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


class Boat():
    def move_boat_right(self):
        i = 0
        for b in self.entire_boat:
            if b.x_coordinate == 10:
                raise OutOfBoardException
        for coordinate in self.entire_boat:
            self.entire_boat[i].set_x(coordinate.x_coordinate + 1)
            i += 1

    def move_boat_left(self):
        i = 0
        for b in self.entire_boat:
            if b.x_coordinate == 1:
                raise OutOfBoardException
        for coordinate in self.entire_boat:
            self.entire_boat[i].set_x(coordinate.x_coordinate - 1)
            i += 1

    def move_boat_up(self):
        i = 0
        for b in self.entire_boat:
            if b.y_coordinate == "A":
                raise OutOfBoardException
        for b in self.entire_boat:
            new_space = movement_board_up.get(b.y_coordinate, None)
            self.entire_boat[i].set_y(new_space)
            i += 1

    def move_boat_down(self):
        i = 0
        for b in self.entire_boat:
            if b.y_coordinate == "J":
                raise OutOfBoardException
        for b in self.entire_boat:
            new_space = movement_board_down.get(b.y_coordinate, None)
            self.entire_boat[i].set_y(new_space)
            i += 1


class Destroyer(Boat):
    def __init__(self):
        self.name = "Destroyer"
        self.entire_boat = [BoatComponent("A", 10), BoatComponent("B", 10)]

    def rotate_destroyer(self):
        if self.entire_boat[0].y_coordinate == self.entire_boat[1].y_coordinate:
            if self.entire_boat[0].y_coordinate == "J":
                raise OutOfBoardException
            self.entire_boat[1].move_singular_down_left()
        else:
            if self.entire_boat[0].x_coordinate == 10:
                raise OutOfBoardException
            self.entire_boat[1].move_singular_right_up()


