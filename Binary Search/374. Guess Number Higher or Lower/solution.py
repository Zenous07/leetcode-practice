def guessNumber(n):
    l=1
    curr=int((l+n)/2)
    while True:
        gus=guess(curr)
        if gus == 0:
            return curr
        if gus == -1:
            n=curr-1
            curr=int((l+n)//2)
        if gus == 1:
            l=curr+1
            curr=int((l+n)//2)
