from sudoku import Sudoku
from sudoku_agent import SudokuAgent

s1 = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
      [6, 0, 0, 1, 9, 5, 0, 0, 0],
      [0, 9, 8, 0, 0, 0, 0, 6, 0],
      [8, 0, 0, 0, 6, 0, 0, 0, 3],
      [4, 0, 0, 8, 0, 3, 0, 0, 1],
      [7, 0, 0, 0, 2, 0, 0, 0, 6],
      [0, 6, 0, 0, 0, 0, 2, 8, 0],
      [0, 0, 0, 4, 1, 9, 0, 0, 5],
      [0, 0, 0, 0, 8, 0, 0, 7, 9]]

s2 = [[1, 0, 0, 0, 0, 0, 0, 0, 6],
      [0, 3, 0, 7, 0, 5, 0, 2, 0],
      [0, 0, 2, 0, 0, 0, 5, 0, 0],
      [0, 7, 0, 8, 0, 9, 0, 3, 0],
      [9, 0, 0, 0, 3, 0, 0, 0, 8],
      [0, 1, 0, 4, 0, 7, 0, 5, 0],
      [0, 0, 6, 0, 0, 0, 9, 0, 0],
      [0, 2, 0, 6, 0, 1, 0, 4, 0],
      [8, 0, 0, 0, 0, 0, 0, 0, 2]]

s3 = [[0, 0, 0, 0, 9, 4, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 6, 0, 7],
      [0, 0, 4, 8, 0, 1, 0, 2, 0],
      [0, 0, 9, 0, 0, 0, 4, 0, 6],
      [4, 0, 0, 0, 2, 0, 0, 0, 1],
      [6, 0, 7, 0, 0, 0, 5, 0, 0],
      [0, 1, 0, 5, 0, 2, 7, 0, 0],
      [3, 0, 5, 0, 0, 0, 0, 0, 0],
      [0, 6, 0, 9, 3, 0, 0, 0, 0]]


# Create an environment
env = Sudoku(s3, True)

# Creat an agent
ag = SudokuAgent(env, True)

# Print CSP
for c in ag.csp:
    for cell in c:
        print(cell)

input('Press ENTER to start')
ag.act()
