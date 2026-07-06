def moveZeros(nums):
    curr=0
    
    for i in range(0,len(nums)):
        if nums[i]!=0:
            nums[curr],nums[i]=nums[i],nums[curr]
            curr+=1

    return nums

print(moveZeros([1,3,0,12,0]))    

