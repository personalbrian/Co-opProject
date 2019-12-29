import GameBoard


class Player:
    def __init__(self):
        self.own_board = GameBoard()
        self.score = 0

    def update(self):
        self.score += 1

