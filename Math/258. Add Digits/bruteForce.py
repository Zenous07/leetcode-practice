def addDigits(num):
    if num <=9:
        return num
    while num >9:
        result=0
        while num >0:
            rem=num%10
            result+=rem
            num=num//10
        num=result
    return result

print(addDigits(38))