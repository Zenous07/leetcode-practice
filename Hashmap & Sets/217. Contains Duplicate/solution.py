def containDuplicate(nums):
    s=set()
    for i in nums:
        if i in s:
            return True
        else:
            s.add(i)
    return False


print(containDuplicate([1,2,3,4,5]))