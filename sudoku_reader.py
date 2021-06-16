import csv


class SudokuReader:

    # def __init__(self):
    #     self.file = file
    #     self.lines = csv.DictReader(self.file)

    def read(self, file):
        lines = csv.DictReader(file)
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

    @staticmethod
    def __get_from_dictionary(line):
        task = line['quizzes']
        solution = line['solutions']
        return task, solution
