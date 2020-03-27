# Loop through all cells in a rows and naked singles
naked_pair = ()
for x in range(9):
    if isinstance(puzzle[x][y], tuple) and len(puzzle[x][y]) == 2 and [_ for _ in puzzle[x] if
                                                                       isinstance(_, tuple)].count(
            puzzle[x][y]) == 2 and naked_pair == ():
        naked_pair = puzzle[x][y]

if naked_pair:
    for y in range(9):
        if isinstance(puzzle[x][y], tuple) and puzzle[x][y] != naked_pair:
            puzzle[x][y] = tuple(item for item in puzzle[x][y] if item not in naked_pair)
            if len(puzzle[x][y]) == 1:
                puzzle[x][y] = puzzle[x][y][0]
                success = True

for y in range(9):
    if isinstance(puzzle[x][y], tuple):
        puzzle[x][y] = 0