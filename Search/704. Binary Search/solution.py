def binary_search(nums,target):
    l=0
    r=len(nums)-1
    m=(l+r)//2
    while l<=r:
        m=(l+r)//2
        if nums[m]==target:
            return m
        elif nums[m]<target:
            l=m+1
        elif nums[m]>target:
            r=m-1
    return -1

print(binary_search([1,2,3,4,5],5))