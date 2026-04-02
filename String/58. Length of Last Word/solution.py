def lengthLastWord(s):
    if len(s)<=1 and s[-1]!=' ': return 1
    count=0
    l=len(s)-1
    while s[l]==' ':
        l=l-1
    if  s[l]!=' ':
        while l>=0 and s[l]!=' ':
            count=count+1
            l=l-1
    return count

print(lengthLastWord("Jesus is God"))