def findMissingNumbers(nums):
    start=min(nums)
    end=max(nums)
    s=set(nums)
    res=[]
    for i in range(start,end+1):
        if i in s:
            continue
        else:
            res.append(i)
    return res

print(findMissingNumbers([3,4,5,6,8]))