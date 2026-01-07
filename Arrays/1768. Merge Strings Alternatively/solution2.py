def alternate(word1,word2):
    a=len(word1)
    b=len(word2)
    newWord=""
    if a>b:
        for i in range(0,b):
            newWord+=word1[i]
            newWord+=word2[i]
        newWord+=word1[b:a]
    elif b>a:
        for i in range(0,a):
            newWord+=word1[i]
            newWord+=word2[i]
        newWord+=word2[a:b]
    else:
        for i in range(0,a):
            newWord+=word1[i]
            newWord+=word2[i]
    return newWord

print(alternate("abcd","1234567"))
    