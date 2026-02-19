def merge(nums1,m,nums2,n):
    if len(nums1)==0 and len(nums2)==0: return []
    result=[]
    l=0
    r=0
    while l<m and r<n:
        if nums1[l]<=nums2[r]: 
            result.append(nums1[l])
            l=l+1
        else:
            print(r)
            result.append(nums2[r])
            r+=1
    if m>=n:
        while l<m:
            result.append(nums1[l])
            l=l+1
    if n>m:
        while r<n:
            result.append(nums2[r])
            r=r+1
    return result

print(merge([1,2,3,0,0,0],3,[2,5,6],3))
