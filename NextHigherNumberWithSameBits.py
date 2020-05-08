def next_higher(value):
    number_of_bits = bin(value).count('1')
    while True:
        value += 1
        if number_of_bits == bin(value).count('1'):
            return value


print(next_higher(1022))
