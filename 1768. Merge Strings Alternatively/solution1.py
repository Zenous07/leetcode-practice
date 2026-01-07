def alternate(word1, word2):
    res = []
    min_len = min(len(word1), len(word2))

    for i in range(min_len):
        res.append(word1[i])
        res.append(word2[i])

    res.append(word1[min_len:])
    res.append(word2[min_len:])

    return ''.join(res)

print(alternate("abcd","1234567"))