import copy


class Solver:

    sudoku_matrix = None
    sudoku_backup = None

    def __init__(self, sudoku_matrix):
        self.sudoku_matrix = sudoku_matrix
        # self.sudoku_backup = None

    def solve(self):
        self.successful_scan()
        if self.not_solved():
            self.guess()
        return self.sudoku_matrix

    def successful_scan(self):
        before = self.not_solved()
        after = 0
        success = 0
        while self.__successful(before, after):
            success += 1
            before = self.not_solved()
            self.scan()
            after = self.not_solved()
        return success

    def guess_failed(self):
        zeros = self.__find_sets()
        for zero in zeros:
            if len(list(zero['candidates'])) < 1:
                return True
        return False

    def __sudoku_backup(self):
        self.sudoku_backup = copy.deepcopy(self.sudoku_matrix)

    def __sudoku_restore(self):
        self.sudoku_matrix = copy.deepcopy(self.sudoku_backup)

    def guess(self):
        if self.not_solved():
            zeros = self.__find_sets()
            self.__sudoku_backup()
            for zero in zeros:
                if not self.not_solved():
                    break
                keep = copy.deepcopy(zero)
                x = keep['x']
                y = keep['y']
                for candidate in keep['candidates']:
                    oh_yeah = 0
                    self.sudoku_matrix[y][x] = candidate
                    if self.successful_scan() and not self.guess_failed():
                        self.__sudoku_backup()
                        oh_yeah += 1
                        break
                    elif self.guess_failed():
                        self.__sudoku_restore()
                if not oh_yeah:
                    continue
                #     oh_yeah = 0
                break
            self.guess()

    def not_solved(self):
        return len(list(self.__find_sets()))

    @staticmethod
    def __successful(before, after):
        return before - after

    def scan(self):
        zeros = self.__find_sets()
        for options in zeros:
            x = options["x"]
            y = options["y"]
            keep_value = options['candidates']
            self.reduce_candidates(x, y)
            if len(options["candidates"]) == 1:
                self.sudoku_matrix[y][x], = options["candidates"]
            elif len(options["candidates"]) == 0:
                options['candidates'] = keep_value
                break

    def reduce_candidates(self, x, y):
        self.reduce_row(x, y)
        self.reduce_column(x, y)
        self.reduce_block(x, y)

    def reduce_row(self, x, y):
        # collapse x
        for row in self.sudoku_matrix:
            if type(row[x]) is not set:
                value = row[x]
                self.discard_values_from_set(x, y, value)

    def reduce_column(self, x, y):
        # collapse y
        for value in self.sudoku_matrix[y]:
            if type(value) is not set:
                self.discard_values_from_set(x, y, value)

    def reduce_block(self, x, y):
        # collapse 9
        x33 = x // 3 * 3
        y33 = y // 3 * 3
        for y333 in range(y33, y33 + 3):
            for x333 in range(x33, x33 + 3):
                value = self.sudoku_matrix[y333][x333]
                if type(value) is not set:
                    self.discard_values_from_set(x, y, value)

    def discard_values_from_set(self, x, y, value):
        self.sudoku_matrix[y][x].discard(value)

    #  Example:
    # {
    #   x: 0,
    #   y: 0,
    #   candidates: { 1, 2, 3, 5, 6, 7, 8, 9}
    # }
    def __find_sets(self):
        for y in enumerate(self.sudoku_matrix):
            for x in enumerate(y[1]):
                if type(x[1]) is set:
                    yield {"x": x[0], "y": y[0], "candidates": x[1]}
