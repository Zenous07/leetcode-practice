def singleNum(nums):
    if len(nums)==0:return []
    if len(nums)==1:return nums[0]
    nums.sort()
    i=0
    while i<len(nums)-1:
        if nums[i]==nums[i+1]:
            i=i+2
        else:
            return nums[i]
    return nums[i]