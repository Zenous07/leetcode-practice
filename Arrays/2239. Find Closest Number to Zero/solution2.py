#sol2
def findClosestNumber(nums):
    result=nums[0]
    for i in nums:
        if abs(i) <= abs(result):
            if abs(result)==abs(i):
                result=max(result,i)
            else:
                result=i
    return result

print(findClosestNumber([2,-1,1]))
