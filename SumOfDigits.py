def digital_root(n: int) -> int:
    root = sum([int(x) for x in str(n)])

    if len(str(root)) == 1:
        return root
    return digital_root(root)


print(digital_root(16))
