import csv


class SudokuReader:

    def __init__(self, file):
        self.f = open(file)

    def read(self):
        lines = csv.DictReader(self.f)
        # sudokus = map(self.__get_from_dictionary, lines)
        return lines

        # for line in lines:
        # task = line['quizzes']
        # solution = line['solutions']
        # print(task, solution)
        # task_matrix = Matrix(task)
        # solution_matrix = Matrix(solution)
        #
        # sudoku = Sudoku(task_matrix, solution_matrix)

    def close(self):
        self.f.close()


    @staticmethod
    def __get_from_dictionary(line):
        task = line['quizzes']
        solution = line['solutions']
        return task, solution
