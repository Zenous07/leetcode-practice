def slidingWindowMax(nums,k):
    result=[]
    win=nums[0:k]
    maxE=max(win)
    l=k
    result.append(maxE)
    print(win)
    for _ in range(len(nums)-k):
        left=win.pop(0)
        right=win.append(nums[l])
        if left>=maxE
        l+=1
        result.append(max(win))
        print(win)
    return result

print(slidingWindowMax([1,3,-1,-3,5,3,6,7],3))