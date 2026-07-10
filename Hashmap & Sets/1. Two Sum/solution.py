def twoSum(nums,target):
    d=dict()
    for i in range(len(nums)):
        rem=target-nums[i]
        if rem in d:
            return [d[rem],i]
        else:
            d[nums[i]]=i
    

print(twoSum([2,7,11,15],9))