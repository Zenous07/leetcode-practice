def twoSum(numbers,target):
    length=len(numbers)
    if length<=1: return False
    l=0
    r=length-1
    while l<r:
        if numbers[l]+numbers[r]==target:
            return [l+1,r+1]
        elif numbers[l]+numbers[r]>target:
            r=r-1
        elif numbers[l]+numbers[r]<target:
            l=l+1
    return False

print(twoSum([2,7,11,15],9))
