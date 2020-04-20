def justify(text: str, width: int) -> str:
    # your code here

    words = text.split(' ')
    line = []
    lines = []
    new_line = 0
    for w in words:
        if (len(line) - 1) + new_line + len(w) < width:
            new_line += len(w)
            line.append(w)
        else:
            lines.append(line)
            line = [w]
            new_line = len(w)
    else:
        lines.append(line)

    for i in range(len(lines)):
        if i != len(lines)-1:
            spaces = width - len(''.join(lines[i]))
            spaces_width = spaces//(len(lines[i])-1)
            for j in range(len(lines[i])):
                if j != len(lines[i])-1:
                    if spaces_width > 0:
                        lines[i][j] += ' '*(spaces_width+1)

    print('\n'.join([''.join([x for x in l]) for l in lines]))

t = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, at elementum ligula ' \
    'tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet felis suscipit tristique. Nam a ' \
    'imperdiet tellus. Nulla eu vestibulum urna. Vivamus tincidunt suscipit enim, nec ultrices nisi volutpat ac. ' \
    'Maecenas sit amet lacinia arcu, non dictum justo. Donec sed quam vel risus faucibus euismod. Suspendisse rhoncus ' \
    'rhoncus felis at fermentum. Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. In vestibulum ' \
    'velit ac felis rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus dapibus. Pellentesque ' \
    'commodo, nisi sit amet hendrerit fringilla, ante odio porta lacus, ut elementum justo nulla et dolor.'
w = 30

print(justify(t, w))
