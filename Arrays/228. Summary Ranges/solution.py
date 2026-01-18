def ranges(nums):
    length=len(nums)
    if length<=0: return []
    if length<=1: return [f"{nums[0]}"]
    firstVal=nums[0]
    lastVal=nums[0]
    newArr=[]
    for i in range(1,length):
        if nums[i-1]==nums[i]-1:
            lastVal=nums[i]
        else:
            if lastVal==firstVal:
                newArr.append(f"{firstVal}")
            else:
                newArr.append(f"{firstVal}->{lastVal}")
            firstVal=nums[i]
            lastVal=nums[i]
    if lastVal==firstVal:
        newArr.append(f"{firstVal}")
    else:
        newArr.append(f"{firstVal}->{lastVal}")
    return newArr

print(ranges([]))