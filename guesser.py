import copy


class Guesser:

    def __init__(self, zeros, sudoku):
        self.fake_matrix = sudoku
        self.zeros = zeros

    def guess(self):
        for zero in self.zeros:
            keep = copy.deepcopy(zero)
            x = keep['x']
            y = keep['y']
            for candidate in keep['candidates']:
                # print(candidate)
                self.fake_matrix[y][x] = candidate
                fake = {'matrix': copy.deepcopy(self.fake_matrix),
                        'x': x, 'y': y, 'candidate': candidate}
                yield fake
            self.fake_matrix[y][x] = keep['candidates']
