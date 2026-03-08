def firstBad(n):
    if n<=1: return n
    l=0
    r=n-1
    while l<=r:
        m=(l+r)//2
        curr=isBadVersion(m)
        if curr:
            r=m-1
        else:
            l=m+1
    return l