def alternateSum(nums):
    sum=0
    for i in range(len(nums)):
        if i %2==0:
            sum+=nums[i]
        else:
            sum-=nums[i]
    return sum

print(alternateSum([1,3,5,7]))