def majorityElement(nums):
    if len(nums)<=1:
        return nums
    cand=None
    count=0
    for i in range(len(nums)):
        if count <=0:
            cand=nums[i]
            count=1
        elif nums[i]==cand:
            count+=1
        else:
            count-=1
    return cand

print(majorityElement([2,5,5]))