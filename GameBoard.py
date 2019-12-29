from Coordinate import Coordinate


def setup():
    main_list = []
    rows_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    i = 0
    while len(main_list) < 10:
        secondary_list = []
        for number in range(1, 11):
            coord = Coordinate()
            coord.set_rows(rows_list[i])
            coord.set_columns(number)
            secondary_list.append(coord)

        i += 1
        main_list.append(secondary_list)
    return main_list


class GameBoard:

    def __init__(self):
        self.matrix = setup()

    def coordinate_finder(self, string, number):
        matrix_dictionary = {
            "A": self.matrix[0],
            "B": self.matrix[1],
            "C": self.matrix[2],
            "D": self.matrix[3],
            "E": self.matrix[4],
            "F": self.matrix[5],
            "G": self.matrix[6],
            "H": self.matrix[7],
            "I": self.matrix[8],
            "J": self.matrix[9],
        }
        list_1 = matrix_dictionary.get(string.upper(), None)
        return list_1[number - 1]

