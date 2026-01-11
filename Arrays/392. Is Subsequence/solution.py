def isSubSequence(s,t):
    a=len(t)
    b=len(s)
    l=0
    r=0
    while l<a and r<b:
        if t[l]==s[r]:
            r=r+1
            l=l+1
        else:
            l=l+1
    
    if r==b:
        return True
    else:
        return False
    
print(isSubSequence("abc","ahbgd"))