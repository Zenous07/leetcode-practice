def palindrome(x):
    if x<0: return False
    else:
        x=str(x)
        if x==x[::-1]: return True
        return False

print(palindrome(777))