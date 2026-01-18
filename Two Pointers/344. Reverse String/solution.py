def rev(s):
    length=len(s)
    if length <=1 :return s
    l=0
    r=length-1
    while l<=r:
        temp=s[l]
        s[l]=s[r]
        s[r]=temp
        l=l+1
        r=r-1
    return s

print(rev(["h","e","l","l","o"]))