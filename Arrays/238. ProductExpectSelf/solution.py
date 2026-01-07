def productExpectSelf(nums):
    answer=[0]*len(nums)
    l=1
    r=1
    larr=[0]*len(nums)
    rarr=[0]*len(nums)
    for i in range(len(nums)):
        j=-i-1
        larr[i]=l
        rarr[j]=r
        l=l*nums[i]
        r=r*nums[j]

    for i in range(len(nums)):
        answer[i]=larr[i]*rarr[i]

    return answer

nums=[1,2,3,4,5]
print(productExpectSelf(nums))