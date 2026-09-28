def maxDepth(s):
    maxDepth=0
    count=0
    for i in s:
        if i=="(":
            count+=1
        if i ==")":
            maxDepth=max(maxDepth,count)
            count-=1
    return maxDepth