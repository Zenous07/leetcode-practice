def addDigits(num):
    if num <=9:
        return num
    if num%9==0:
        return 9
    else:
        return num%9

print(addDigits(38))