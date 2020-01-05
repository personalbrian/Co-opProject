from GameBoard import GameBoard
import Boat
import BoatComponent
import Coordinate


class BoatAlreadyOnException(Exception):
    pass


class Player:
    def __init__(self):
        self.own_board = GameBoard()
        self.score = 0
        self.destroyer = Boat.Destroyer()
        self.submarine = Boat.Submarine()
        self.destroyer_placed = False
        self.submarine_placed = False

    def update(self):
        self.score += 1

    def confirm_placement_destroyer(self):
        for b in self.destroyer.entire_boat:
            string = b.y_coordinate
            num = b.x_coordinate
            coordinate = self.own_board.coordinate_finder(string, num)
            coordinate.boat_true()
        self.destroyer_placed = True

    def confirm_placement_submarine(self):
        for b in self.submarine.entire_boat:
            string = b.y_coordinate
            num = b.x_coordinate
            coordinate = self.own_board.coordinate_finder(string, num)
            if coordinate.boat_on:
                raise BoatAlreadyOnException
        for b in self.submarine.entire_boat:
            string = b.y_coordinate
            num = b.x_coordinate
            coordinate = self.own_board.coordinate_finder(string, num)
            coordinate.boat_true()


