class Guesser:

    def __init__(self, zeros, sudoku):
        self.sudoku_matrix = sudoku
        self.zeros = zeros

    def guess(self):
        oh_yeah = 0
        if self.not_solved(self.sudoku_matrix):
            self.zeros = self.__find_sets(self.sudoku_matrix)
            self.__sudoku_backup()
            for zero in self.zeros:
                if not self.not_solved(self.sudoku_matrix):
                    break
                keep = copy.deepcopy(zero)
                x = keep['x']
                y = keep['y']
                for candidate in keep['candidates']:
                    oh_yeah = 0
                    self.sudoku_matrix[y][x] = candidate
                    if self.successful_scan(self.sudoku_matrix) and not self.guess_failed():
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