def trap(height):
    left=[0]*len(height)
    right=[0]*len(height)
    leftMax=0
    rightMax=0
    count=0
    for i in range(len(height)):
        j=-i-1
        leftMax=max(leftMax,height[i])
        left[i]=leftMax
        rightMax=max(rightMax,height[j])
        right[j]=rightMax
    for i in range(len(height)):
        count+=min(left[i],right[i])-height[i]
    
    return count

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))