def insertPosition(nums,target):
    l=0
    r=len(nums)-1
    while l<=r:
        m=(l+r)//2
        if nums[m]==target:
            return m
        elif nums[m]<target:
            l=m+1
        elif nums[m]>target:
            r=m-1
    return l

print(insertPosition([1,3,5,6],7))