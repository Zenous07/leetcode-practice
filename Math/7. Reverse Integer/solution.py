def revInt(x):
    rev=0
    sign = 1 if x >= 0 else -1
    x=sign*x
    while x!=0:
        temp=x%10
        rev=rev*10+temp
        x=x//10
    rev=rev*sign
    if -2**31<=rev<=2**31-1:
        return rev
    return 0


print(revInt(-123))