def searchInsert(nums,target):
    i=0
    while i<len(nums) and target>nums[i]:
        i=i+1
    if i+1==len(nums): return i
    return i

print(searchInsert([1,3,5,6],7))