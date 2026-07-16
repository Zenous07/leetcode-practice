def trap(height):
    l=0
    r=len(height)-1
    leftMax=0
    rightMax=0
    count=0
    while l<r:
        leftMax=max(leftMax,height[l])
        rightMax=max(rightMax,height[r])
        if height[r]<height[l]:
            count+=rightMax-height[r]
            r-=1
        else:
            count+=leftMax-height[l]
            l+=1
    return count

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))