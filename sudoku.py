from solver import *


class Sudoku:
    def __init__(self, task, solution):
        self.task = task
        self.solution = solution

    def check(self):
        solver = Solver(sudoku)
        solver.solve()
        # solver.check_set_size()

        return sudoku.board == solution.board

