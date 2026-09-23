def findMedianSortedArrays(nums1,nums2):
    m=len(nums1)
    n=len(nums2)
    res=[]
    even=False
    if (m+n) % 2 == 0:
        even=True
        len_middle=int((m+n)/2)+1
    else:
        len_middle=(m+n)//2+1
    l=0
    r=0
    temp=True
    while temp:
        if l<m and r<n and len(res)<len_middle:
            if nums1[l]<=nums2[r]:
                res.append(nums1[l])
                l+=1
            elif nums1[l]>nums2[r]:
                res.append(nums2[r])
                r+=1
        elif l<m and len(res)<len_middle:
            res.append(nums1[l])
            l+=1
        elif r<n and len(res)<len_middle:
            res.append(nums2[r])
            r+=1
        elif len(res)==len_middle:
            temp=False
    if even:
        return (res[-1]+res[-2])/2
    return float(res[-1])