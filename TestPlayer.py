import unittest
from Player import Player
from Player import BoatAlreadyOnException


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def test_confirm_destroyer(self):
        self.player.confirm_placement_destroyer()
        coord = self.player.own_board.coordinate_finder("A", 10)
        self.assertTrue(coord.boat_on)

    def test_confirm_submarine(self):
        try:
            self.player.confirm_placement_destroyer()
            coord = self.player.own_board.coordinate_finder("A", 10)
            self.assertTrue(coord.boat_on)
        except BoatAlreadyOnException:
            print("fail")

    def test_boat_exception(self):
        try:
            self.player.confirm_placement_destroyer()
            self.player.confirm_placement_submarine()
        except BoatAlreadyOnException:
            print("success")


