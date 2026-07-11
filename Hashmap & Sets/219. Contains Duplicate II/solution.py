def containsDuplicate(nums,k):
    d=dict()
    for i in range(len(nums)):
        if nums[i] not in d:
            d[nums[i]]=i
        else:
            if abs(d[nums[i]]-i)<=k:
                return True
            else:
                d[nums[i]]=i
    return False

print(containsDuplicate([1,2,3,1],3))