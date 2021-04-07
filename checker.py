class Checker:

    def __init__(self, task, solution):
        self.task = task
        self.solution = solution

    def solved(self):
        solved = self.task == self.solution
        return solved
