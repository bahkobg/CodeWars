def recoverSecret(triplets):
    repeat = 1
    word = {}
    for t in triplets:
        word.update({k: 0 for k in t})

    while repeat > 0:
        for t in triplets:
            if word[t[2]] <= word[t[1]]:
                word[t[2]] = word[t[1]] + 1
                repeat += 1
            elif word[t[1]] <= word[t[0]]:
                word[t[1]] = word[t[0]] + 1
                repeat += 1
        repeat -= 1

    return ''.join([key for (key, value) in sorted(word.items(), key=lambda x: x[1])])


triplets = [
    ['t', 'u', 'p'],
    ['w', 'h', 'i'],
    ['t', 's', 'u'],
    ['a', 't', 's'],
    ['h', 'a', 'p'],
    ['t', 'i', 's'],
    ['w', 'h', 's']
]

print(recoverSecret(triplets))
