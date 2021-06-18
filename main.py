from sudoku_reader import *
from matrix import *
from checker import *
from solver import *
import argparse

parser = argparse.ArgumentParser(description='give me some sudokus')

FILE = 'sudoku_examples.csv'

solved_count = 0
unsolved_count = 0

reader = SudokuReader(FILE)
sudokus = reader.read() # returns a dict with 'quizzes' and 'solutions'

for sudoku in sudokus:
    task = Matrix(sudoku['quizzes'])
    solution = Matrix(sudoku['solutions'])
    print('Task')
    task.show()
    print('Solution')
    solution.show()
    solver = Solver(task.matrix)
    task.matrix = solver.solve()

    print('Task solved')
    task.show()
    checker = Checker(task.matrix, solution.matrix)

    if checker.solved():
        solved_count += 1
    else:
        unsolved_count += 1

    print('correct', solved_count)
    print('incorrect', unsolved_count)
    input('Next?')
reader.close()
