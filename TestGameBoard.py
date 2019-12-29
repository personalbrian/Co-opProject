import unittest
from GameBoard import GameBoard
from Coordinate import Coordinate


class TestGameBoard(unittest.TestCase):

    def setUp(self):
        self.coord = GameBoard()

    def test_coordinate_finder(self):
        dummy_coordinate = Coordinate()
        dummy_coordinate.set_rows("A")
        dummy_coordinate.set_columns(1)
        actual_coordinate = self.coord.coordinate_finder("A", 1)
        string = actual_coordinate.rows
        num = actual_coordinate.columns
        self.assertEqual(dummy_coordinate.rows, string)
        self.assertEqual(dummy_coordinate.columns, num)
