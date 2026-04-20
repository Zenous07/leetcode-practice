def jewelsAndStones(jewels,stones):
    #jewels => n
    #stones => m
    #time complexity => O(n*m)
    count=0
    for i in stones:
        if i in jewels:
            count+=1
    return count

print(jewelsAndStones("aA","aAAbbbb"))