def jewelsAndStones(jewels,stones):
    #jewels => n
    #stones => m
    #time complexity => O(n+m)
    count=0
    s=set(jewels)
    for i in stones:
        if i in s:
            count+=1
    return count

print(jewelsAndStones("aA","aAAbbbb"))