#sol1
def findClosestNumber(nums):
    result=nums[0]
    if nums[0]<0:
        temp_result=nums[0]*-1
    else:
        temp_result=nums[0]
    for i in nums:
        temp=i
        if temp<0:
            temp=temp*-1
        if temp <= temp_result:
            if temp==temp_result:
                result=max(result,i)
            else:
                result=i
                temp_result=temp
    return result

print(findClosestNumber([2,-1,1]))
