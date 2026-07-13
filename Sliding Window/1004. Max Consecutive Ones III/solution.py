def maxConsecutiveOnes(nums,k):
    l=0
    max_w=0
    num_zeros=0
    for r in range(len(nums)):
        if nums[r]==0:
            num_zeros+=1
        while num_zeros>k:
            if nums[l]==0:
                num_zeros-=1
            l+=1
        max_w=max(max_w,r-l+1)
    return max_w

print(maxConsecutiveOnes([1,1,1,0,0,0,1,1,1,1,0],2))