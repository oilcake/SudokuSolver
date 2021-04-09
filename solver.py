from zero_seeker import *
from scaner import *
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
        zeros = self.__find_sets(self.sudoku_matrix)
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
            zeros = self.__find_sets(self.sudoku_matrix)
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
        return len(list(self.__find_sets(self.sudoku_matrix)))

    @staticmethod
    def __successful(before, after):
        return before - after

    def scan(self):
        scaner = Scaner()
        zeros = self.__find_sets(self.sudoku_matrix)
        scaner.scan(zeros)
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

    #  Example:
    # {
    #   x: 0,
    #   y: 0,
    #   candidates: { 1, 2, 3, 5, 6, 7, 8, 9}
    # }
    @staticmethod
    def __find_sets(sudoku):
        seeker = ZeroSeeker(sudoku)
        zeros = seeker.seek()
        return zeros
