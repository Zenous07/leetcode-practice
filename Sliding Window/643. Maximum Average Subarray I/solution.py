def maxAvgSubArr(nums,k):
    if len(nums)<k:
        return 0
    curr=sum(nums[:k])
    maxAvg=curr/k
    for i in range(k,len(nums)):
        curr+=nums[i]
        curr-=nums[i-k]
        maxAvg=max(maxAvg,curr/k)
    return maxAvg

print(maxAvgSubArr([1,12,-5,-6,50,3],4))