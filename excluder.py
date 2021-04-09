class Excluder:

    sudoku_matrix = []

    def exclude(self, zeros, sudoku):
        self.sudoku_matrix = sudoku
        for options in zeros:
            x = options["x"]
            y = options["y"]
            keep_value = options['candidates']
            self.reduce_candidates(x, y)
            if len(options["candidates"]) == 1:
                sudoku[y][x], = options["candidates"]
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

