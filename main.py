from sudoku_reader import *
from matrix import *
from checker import *
from solver import *
import argparse

parser = argparse.ArgumentParser(description='give me some sudokus')

# FILE = '/Users/Oilcake/PycharmProjects/examples/sudoku.csv'

FILE = 'sudoku_examples.csv'


solved_count = 0
unsolved_count = 0

# with open(FILE) as csvfile:
reader = SudokuReader(FILE)
sudokus = reader.read()
count = 0

for sudoku in sudokus:
    count += 1
    # if count < 39030:
    #     continue

    # returns a dict with 'quizzes' and 'solutions'
    task = Matrix(sudoku['quizzes'])
    solution = Matrix(sudoku['solutions'])
    # task.show()
    # print()
    # solution.show()
    # print()
    solver = Solver(task.matrix)
    answer = solver.solve()
    task.matrix = answer

    # task.show()
    # print()
    # solution.show()
    # print()
    checker = Checker(task.matrix, solution.matrix)

    # print(checker.solved())

    if checker.solved():
        solved_count += 1
    else:
        unsolved_count += 1
        # break

    print(solved_count, unsolved_count)
    # input('Next?')
reader.close()
