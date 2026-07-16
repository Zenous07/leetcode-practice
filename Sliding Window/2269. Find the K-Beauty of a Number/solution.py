def kBeauty(num,k):
    snum=str(num)
    if len(snum)<k:
        return 0
    win=snum[0:k]
    val=int(win)
    l=0
    count=0
    for r in range(k+1,len(snum)):
        if num%val==0:
            count+=1
        else:
            val-=int(snum[l]*(10**k))
            l+=1
            val+=int(snum[r])
    return count

print(kBeauty(240,2))
