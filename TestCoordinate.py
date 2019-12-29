import unittest
from Coordinate import Coordinate


class TestCoordinate(unittest.TestCase):

    def setUp(self):
        self.coord = Coordinate()

    def test_set_rows(self):
        row_coords = self.coord
        row_coords.set_rows("A")
        self.assertEqual("A", row_coords.rows)

    def test_set_columns(self):
        column_coords = self.coord
        column_coords.set_columns(10)
        self.assertEqual(10, column_coords.columns)

    def test_hit(self):
        hit_coords = self.coord
        hit_coords.boat_hit()
        self.assertTrue(hit_coords.hitSpace)
