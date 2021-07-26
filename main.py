from reader import *
from matrix import *
from checker import *
from solver import *
import argparse

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

parser = argparse.ArgumentParser(description='give me some sudokus')
parser.add_argument('sudokus', type=str, help='.csv with unsolved sudokus')
args = parser.parse_args()

answer_1 = input('Do you want to see matrixes?(yes/no)')
to_print = str2bool(answer_1)

answer_2 = input('One at a time?(yes/no)')
one = str2bool(answer_2)

solved_count = 0
unsolved_count = 0

reader = Reader(args.sudokus)
sudokus = reader.read() # returns a dict with 'quizzes' and 'solutions'

for sudoku in sudokus:
    task = Matrix(sudoku['quizzes'])
    solution = Matrix(sudoku['solutions'])
    if to_print:
        print('Task')
        task.show()
        print('Solution')
        solution.show()
    solver = Solver(task.matrix)
    task.matrix = solver.solve()
    if to_print:
        print('Task solved')
        task.show()
    checker = Checker(task.matrix, solution.matrix)

    if checker.solved():
        solved_count += 1
    else:
        unsolved_count += 1

    print('correct', solved_count)
    print('incorrect', unsolved_count)
    if one:
        input('hit any key to process next one')
reader.close()
