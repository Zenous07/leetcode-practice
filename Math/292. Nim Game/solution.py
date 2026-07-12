def nimGame(n):
    if n<=2:
        return True
    if n%4==0:
        return False
    return True

print(nimGame(7))