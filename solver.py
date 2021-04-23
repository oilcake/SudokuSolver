from zero_seeker import *
from excluder import *
from guesser import *
import copy


class Solver:

    sudoku_matrix = None
    sudoku_backup = None
    excluder = Excluder()

    def __init__(self, sudoku_matrix):
        self.sudoku_matrix = sudoku_matrix

    def solve(self):
        self.successful_scan(self.sudoku_matrix)
        while self.not_solved(self.sudoku_matrix):
            self.guess()
            self.successful_scan(self.sudoku_matrix)
        return self.sudoku_matrix

    def successful_scan(self, sudoku):
        before = self.not_solved(sudoku)
        after = 0
        success = 0
        while self.__successful(before, after):
            success += 1
            before = self.not_solved(sudoku)
            self.scan(sudoku)
            after = self.not_solved(sudoku)
        return success

    def guess_failed(self, sudoku):
        zeros = self.__find_sets(sudoku)
        for zero in zeros:
            if len(list(zero['candidates'])) < 1:
                return True
        return False

    def guess(self):
        sudoku_copy = copy.deepcopy(self.sudoku_matrix)
        guesser = Guesser(self.__find_sets(sudoku_copy), sudoku_copy)
        fake_collection = guesser.guess()
        for fake in fake_collection:
            fake_matrix = fake['matrix']
            x = fake['x']
            y = fake['y']
            candidate = fake['candidate']
            self.successful_scan(fake_matrix)
            if self.guess_failed(fake_matrix):
                self.sudoku_matrix[y][x].discard(candidate)

    def not_solved(self, sudoku):
        return len(list(self.__find_sets(sudoku)))

    @staticmethod
    def __successful(before, after):
        return before - after

    def scan(self, sudoku):
        zeros = self.__find_sets(sudoku)
        self.excluder.exclude(zeros, sudoku)

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
