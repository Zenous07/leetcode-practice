def minSizeSubarr(nums,target):
    l=0
    result=len(nums)+1
    sum=0
    for r in range(0,len(nums)):
        sum+=nums[r]
        while sum>=target:
            result=min(result,r-l+1)
            sum-=nums[l]
            l+=1
    if result==len(nums)+1:
        return 0
    return result

print(minSizeSubarr([2,3,1,2,4,3],7))