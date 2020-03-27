def break_pieces(shape):
    shape = shape.split('\n')
    coordinates = []
    for x in range(len(shape)):
        for y in range(len(shape[x])):
            if shape[x][y] == '+':
                coordinates.append((x, y))
    print(coordinates)



shape = '\n'.join(["+------------+",
                   "|            |",
                   "|            |",
                   "|            |",
                   "+------+-----+",
                   "|      |     |",
                   "|      |     |",
                   "+------+-----+"])
print(break_pieces(shape))
