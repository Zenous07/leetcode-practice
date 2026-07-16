def squaresOfSortedArray(nums):
    result=[0]*len(nums)
    l=0
    r=len(nums)-1
    k=-1
    while l<r:
        if nums[l]**2 >= nums[r]**2:
            result[k]=nums[l]**2
            l+=1
            k-=1
        else:
            result[k]=nums[r]**2
            r-=1
            k-=1
    return result

print(squaresOfSortedArray([-7,-3,2,3,11]))