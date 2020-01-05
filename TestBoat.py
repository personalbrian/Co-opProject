import unittest
from Boat import Destroyer
from Boat import OutOfBoardException
from Boat import Submarine


class TestBoat(unittest.TestCase):
    def setUp(self):
        self.destroyer = Destroyer()
        self.submarine = Submarine()

    def test_move_down(self):
        self.destroyer.move_boat_down()
        string = self.destroyer.entire_boat[0].y_coordinate
        self.assertEqual("B", string)

    def test_rotate_destroyer(self):
        self.destroyer.move_boat_left()
        self.destroyer.rotate_destroyer()
        string_1 = self.destroyer.entire_boat[0].y_coordinate
        self.assertEqual("A", string_1)
        string_2 = self.destroyer.entire_boat[1].y_coordinate
        self.assertEqual("A", string_2)
        number_1 = self.destroyer.entire_boat[0].x_coordinate
        self.assertEqual(9, number_1)

    def test_move_right(self):
        self.destroyer.move_boat_left()
        self.destroyer.move_boat_left()
        self.destroyer.move_boat_right()
        number_1 = self.destroyer.entire_boat[0].x_coordinate
        self.assertEqual(9, number_1)

    def test_out_of_board_exception(self):
        try:
            self.destroyer.move_boat_right()
            print("fail")
        except OutOfBoardException:
            print('Success')

    def test_out_of_bound_rotate(self):
        try:
            self.destroyer.rotate_destroyer()
            print("fail")
        except OutOfBoardException:
            print("Success")

    def test_rotate_submarine(self):
        try:
            self.submarine.move_boat_left()
            self.submarine.move_boat_left()
            self.submarine.rotate_submarine()
            num = self.submarine.entire_boat[0].x_coordinate
            self.assertEqual(8, num)
        except OutOfBoardException:
            print("fail")

    def test_rotate_bound_submarine(self):
        try:
            self.submarine.rotate_submarine()
            print("fail")
        except OutOfBoardException:
            print("Success")
