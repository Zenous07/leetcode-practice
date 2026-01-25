def threeSum(nums):
    length=len(nums)
    if length <=2: return []
    nums.sort()
    result=[]
    for curr in range(0,length-1):
        if nums[curr]>0:
            break
        elif curr>0 and nums[curr]==nums[curr-1]:
            continue
        l=curr+1
        r=length-1
        while l<r:
            sum=nums[l]+nums[r]+nums[curr]
            if sum==0:
                result.append([nums[l],nums[r],nums[curr]])
                l=l+1
                r=r-1
                while l<r and nums[l]==nums[l-1]:
                    l=l+1
                while l<r and nums[r]==nums[r+1]:
                    r=r-1
            elif sum>0:
                r=r-1
            else:
                l=l+1
    return result

print(threeSum([-1,0,1,2,-1,-4]))