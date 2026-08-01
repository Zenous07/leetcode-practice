def findWords(words,x):
    result=[]
    for i in range(len(words)):
        s=set(words[i])
        if x in s:
            result.append(i)
    return result

print(findWords(["leet","code"],"e"))