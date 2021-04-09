class ZeroSeeker:

    def __init__(self, matrix):
        self.matrix = matrix

    def seek(self):
        for y in enumerate(self.matrix):
            for x in enumerate(y[1]):
                if type(x[1]) is set:
                    yield {"x": x[0], "y": y[0], "candidates": x[1]}
