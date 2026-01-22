def he(height):
    l=0
    r=len(height)-1
    maxV=0
    while l<=r:
        maxH=min(height[l],height[r])
        dist=r-l
        maxV=max(maxV,maxH*dist)
        if height[l]<=height[r]:
            l=l+1
        else:
            r=r-1
    return maxV

print(he([1,100,1]))