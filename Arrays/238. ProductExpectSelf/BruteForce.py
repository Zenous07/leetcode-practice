def productExpectSelf(nums):
    l=0
    r=0
    tempSum=1
    newNums=[]
    while r<len(nums):
        while l<len(nums):
            if l==r:
                l=l+1
            else:
                tempSum=tempSum*nums[l]
                l=l+1
        r=r+1
        newNums.append(tempSum)
        tempSum=1
        l=0
    return newNums

nums=[1,2,3,4,5]
print(productExpectSelf(nums))