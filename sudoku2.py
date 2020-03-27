class Sudoku:

    def __init__(self, board):
        self.board = board

    def __new__(cls, board):
        if not isinstance(board, list) or len(board) != 9:
            return None
        else:
            return object.__new__(cls)

    def __repr__(self):
        for row in self.board:
            print(row)

    def get_rows(self):
        return [[self.board[j][i] for i in range(9)] for j in range(9)]

    def get_columns(self):
        return [[self.board[j][i] for j in range(9)] for i in range(9)]

    def get_little_squares(self):
        return [[self.board[i + x][j + y] for x in range(3) for y in range(3)] for i in range(0, 9, 3) for j in
                range(0, 9, 3)]

    def iterate(self):
        _success = False
        for x in range(9):  # Loop through all rows
            for y in range(9):  # Loop through all cells in a rows and search for naked singles
                if self.board[x][y] == 0:
                    guess = [x for x in range(1, 10)]
                    guess = [n for n in guess if
                             n not in self.get_rows()[x] and n not in self.get_columns()[x] and n not in
                             self.get_little_squares()[3 * (x // 3) + y // 3]]

                    if len(guess) == 1:  # If naked single is found, replace the cell value
                        self.board[x][y] = guess[0]
                        _success = True  # Signaling the outer func to loop through again
        return self.board, _success

    def solve(self):
        while self.iterate()[1]:
            self.board = self.iterate()[0]
        return self.board


puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]

solved = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
          [6, 7, 2, 1, 9, 5, 3, 4, 8],
          [1, 9, 8, 3, 4, 2, 5, 6, 7],
          [8, 5, 9, 7, 6, 1, 4, 2, 3],
          [4, 2, 6, 8, 5, 3, 7, 9, 1],
          [7, 1, 3, 9, 2, 4, 8, 5, 6],
          [9, 6, 1, 5, 3, 7, 2, 8, 4],
          [2, 8, 7, 4, 1, 9, 6, 3, 5],
          [3, 4, 5, 2, 8, 6, 1, 7, 9]]


