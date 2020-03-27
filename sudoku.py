class Sudoku():
    # Convert every cell to string upon initializing
    def __init__(self, board):
        self.board = [[str(board[j][i]) for i in range(9)]
                      for j in range(9)]

    # Check if the board is 9x9 cells and all cells are integers 1...9
    def __new__(cls, board):
        if isinstance(board, list) and len(board) == 9:
            for row in board:
                if isinstance(row, list) and len(row) == 9:
                    for item in row:
                        if isinstance(item, int) and item in [x for x in range(10)]:
                            pass
                        else:
                            return None
                else:
                    return None
        else:
            return None

        return object.__new__(cls)

    # Define user-friendly representation
    def __str__(self):
        display = ''
        for i in range(9):
            display += ' '.join(c if c != '0' and len(c) == 1 else '.' for c in self.board[i]) + '\n'
        return display

    # Define all possibilities for troubleshooting
    def __repr__(self):
        display = ''
        for i in range(9):
            display += ' '.join(c if c != '0' else '.' for c in self.board[i]) + '\n'
        return display

    def _get_peers(self,x,y):
        _rows = [[str(self.board[j][i]) for i in range(9)]
                      for j in range(9)]
        _columns = [[str(self.board[j][i]) for j in range(9)]
                    for i in range(9)]
        _little_squares = [[str(self.board[i + x][j + y]) for x in range(3)
                            for y in range(3)]
                           for i in range(0, 9, 3)
                           for j in range(0, 9, 3)]
        return [_rows[x], _columns[y], _little_squares[3 * (x // 3) + y // 3]]

    # Iterate through all possibilities
    def _iterate(self):
        _done = True
        _columns = [[str(self.board[j][i]) for j in range(9)]
                    for i in range(9)]
        _little_squares = [[str(self.board[i + x][j + y]) for x in range(3)
                            for y in range(3)]
                           for i in range(0, 9, 3)
                           for j in range(0, 9, 3)]
        for x in range(9):  # Loop through all rows
            for y in range(9):  # Loop through all cells in a rows and search for naked singles
                if self.board[x][y] == '0' or len(self.board[x][y]) > 1:
                    guess = [str(x) for x in range(1, 10)]
                    guess = [n for n in guess if
                             n not in self.board[x] and n not in _columns[y] and n not in _little_squares[
                                 3 * (x // 3) + y // 3]]
                    if len(guess) == 1:  # If naked single is found, replace the cell value
                        self.board[x][y] = guess[0]
                        _done = False  # Signaling the outer func to loop through again
                    else:
                        self.board[x][y] = ''.join(c for c in guess)

            for y in range(9):
                # Looking for cells with length 2
                if len(self.board[x][y]) == 2:
                    # Looking for NAKED PAIRS in rows
                    if self.board[x].count(self.board[x][y]) == 2:
                        print("FOUND NAKED PAIR IN ROW {}".format(x))
                        # Loop through the row again and remove the naked pair from the other cells
                        for j in range(9):
                            if self.board[x][j] != self.board[x][y]:
                                if self.board[x][y][0] in self.board[x][j]:
                                    self.board[x][j] = self.board[x][j].replace(self.board[x][y][0], '').replace(self.board[x][y][1], '')
                                    _done = False  # Signaling the outer func to loop through again
                    # Looking for NAKED PAIRS in columns
                    if _columns[y].count(self.board[x][y]) == 2:
                        print("FOUND NAKED PAIR IN COLUMN {}".format(y))
                    # Looking for NAKED PAIRS in little squares
                    if _little_squares[3 * (x // 3) + y // 3].count(self.board[x][y]) == 2:
                        print("FOUND NAKED PAIR IN LITTLE SQUARE {}".format(3 * (x // 3) + y // 3))

        print("INTERATION *************")

        # If there aren't any naked singles anymore, return the board
        if _done:
            return self.board

        # Iterate again
        return self._iterate()


puzzle = [[0, 0, 5, 0, 0, 0, 8, 0, 0], [0, 2, 0, 8, 0, 9, 0, 7, 0], [3, 0, 0, 0, 4, 0, 0, 0, 1], [0, 3, 0, 2, 0, 6, 0, 1, 0], [0, 0, 2, 0, 0, 0, 5, 0, 0], [0, 7, 0, 5, 0, 4, 0, 6, 0], [2, 0, 0, 0, 6, 0, 0, 0, 4], [0, 8, 0, 4, 0, 2, 0, 9, 0], [0, 0, 7, 0, 0, 0, 2, 0, 0]]



s = Sudoku(puzzle)
print(s)
s._iterate()
print(s)
peers = ['14679', '1469', '5', '136', '123', '13', '8', '34', '369']

for cell in peers:
    for c in cell:
        occurence = 0
        for i in range(9):
            if peers[i].count(c) == 1:
                occurence += 1
        if occurence == 3:
            print("THIS NUM {} IS IN {} CELLS".format(c,occurence))
