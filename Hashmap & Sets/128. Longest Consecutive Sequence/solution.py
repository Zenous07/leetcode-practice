def longestConsecutiveSequence(nums):
    if not nums:
        return 0
    s=set(nums)
    maxCount=0
    count=0
    maxCount=0
    for num in s:
        if num-1 not in s :
            temp=num
            while temp in s:
                count+=1
                temp+=1
            maxCount=max(maxCount,count)
            count=0
    return maxCount


print(longestConsecutiveSequence([100,4,200,1,3,2]))