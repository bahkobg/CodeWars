def code(strng: str) -> str:
    """
    a) Let k be the number of bits of n

    b) Put k-1 times the digit 0 followed by the digit 1

    c) Put number n in binary

    d) Concat the result of b) and c)

    """
    result = ''
    for x in strng:
        k = len(bin(int(x)))-2
        if int(x) == 0:
            b = '10'
        elif int(x) == 1:
            b = '11'
        else:
            b = '01'*(k-1)
        c = bin(int(x))[2:]
        d = b+c
        result += d

    return result




def decode(strng):
    pass

print(code("10111213") == '11101111110110110111')