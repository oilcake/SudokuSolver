class Matrix:

    def __init__(self, quiz):
        # creates a matrix of zeros
        self.matrix = [[0] * 9 for _ in range(9)]
        # fills it with actual sudoku numbers
        for letter in enumerate(quiz):
            x = letter[0] % 9
            y = letter[0] // 9
            number = int(letter[1])
            # creates a set of 123456789 on each zero
            if number == 0:
                number = set(i for i in range(1, 10))
            self.matrix[y][x] = number

    def show(self):
        # just print function
        for y in self.matrix:
            for x in y:
                if type(x) is set:
                    print('0', end=' ')
                else:
                    print(x, end=' ')
            print()

