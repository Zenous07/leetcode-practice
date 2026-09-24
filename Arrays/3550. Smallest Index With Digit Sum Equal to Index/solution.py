def smallestIndex(nums):
    for i in range(len(nums)):
        temp=0
        while nums[i]:
            temp+=nums[i]%10
            nums[i]=nums[i]//10
        if temp == i:
            return temp
    return -1