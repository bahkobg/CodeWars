row = [1, 8, (2, 6, 7), (2, 6), 3, (2, 6), (2, 5, 6), 9, (4, 5)]

for y in range(9):
    if isinstance(row[y], tuple) and len(row[y]) == 2:
        if [x for x in row if isinstance(x, tuple)].count(row[y]) == 2:
            print('FOUND NAKED PAIR - {}'.format(i))


