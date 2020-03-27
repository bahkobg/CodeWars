class Battlefield():

    def __init__(self, field):
        self.field = field
        self.columns = []
        self.rows = []
        self.ships_found = []
        self.ships = {
            1: '1111',
            2: '111',
            3: '11',
            4: '1'
        }

    def __str__(self):
        _field = 'There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1).  \n'.upper()
        _field += 'Each ship must be a straight line, except for submarines, which are just single cell. \n'.upper()
        _field += 'The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner. \n'.upper()
        for row in self.field:
            _field += '  '.join([str(row[y]) if row[y] != 0 else '.' for y in range(10)]) + '\n'
        return _field

    def evaluate(self):
        _adjacent_cells = [(0, 1), (-1, 0), (-1, 1), (1, 1), (1, 0), (1, -1), (-1, -1), (0, -1)]
        _overlap = False

        for k, v in self.ships.items():
            # print("SHIP {}, COUNT {}".format(v, k))
            for i in range(k):
                self.columns = [''.join([str(self.field[x][y]) for x in range(10)]) for y in range(10)]
                self.rows = [''.join([str(self.field[y][x]) for x in range(10)]) for y in range(10)]
                for x in range(10):
                    if self.ships[k] in self.rows[x]:
                        # print("BATTLESHIP FOUND -> SHIP {}, COUNT {}".format(v, k))
                        self.ships_found.append(self.ships[k])
                        y = self.rows[x].find(self.ships[k])

                        for j in range(len(self.ships[k])):
                            if j + y < y + len(self.ships[k]):
                                for adj in _adjacent_cells[1:]:
                                    if 10 > x + adj[0] >= 0 and 10 > j + y + adj[1] >= 0 and self.field[x + adj[0]][j + y + adj[1]] == 1:
                                        _overlap = True
                            elif j + y == y + len(self.ships[k]):
                                for adj in _adjacent_cells[:6]:
                                    if 10 > x + adj[0] >= 0 and 10 > j + y + adj[1] >= 0 and self.field[x + adj[0]][j + y + adj[1]] == 1:
                                        _overlap = True

                            self.field[x][j + y] = 0
                        break
                    elif self.ships[k] in self.columns[x]:
                        # print("BATTLESHIP FOUND -> SHIP {}, COUNT {}".format(v, k))
                        self.ships_found.append(self.ships[k])
                        y = self.columns[x].find(self.ships[k])
                        for j in range(len(self.ships[k])):
                            if j + y < y + len(self.ships[k]):
                                for adj in _adjacent_cells[1:]:
                                    if 10 > j + y + adj[1] >= 0 and 10 > x + adj[0] >= 0 and self.field[j + y + adj[1]][x + adj[0]] == 1:
                                        _overlap = True
                            elif j + y == y + len(self.ships[k]):
                                for adj in _adjacent_cells[:6]:
                                    if 10 > j + y + adj[1] >= 0 and 10 > x + adj[0] >= 0 and self.field[j + y + adj[1]][x + adj[0]] == 1:
                                        _overlap = True
                            self.field[j + y][x] = 0
                        break
        for row in self.field:
            if '1' in ''.join([str(row[y]) for y in range(10)]):
                return False
        return True if self.ships_found == ['1111', '111', '111', '11', '11', '11', '1', '1', '1', '1'] and _overlap is False else False


battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

test = Battlefield(battleField)
print(test)
print(test.evaluate())
print(test)
