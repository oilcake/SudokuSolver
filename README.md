# Sudoku solver

Provides a set of classes to solve sudokus

Solves 1000000 sudokus

__Usage__

```
usage:
main.py [-h] sudokus

positional arguments:
  sudokus     .csv with unsolved sudokus

optional arguments:
  -h, --help  show this help message and exit
```

[download 1000000 sudokus](https://drive.google.com/file/d/1tH7WqOxoG-9k5lRZlEU4HM_mHh10_HlD/view?usp=sharing)

__Sudoku_reader__ - reads csv file with sudoku examples

__Matrix__ - builds a matrix from task

__Solver__ - solves task

__Checker__ - compares computed solution with given one
