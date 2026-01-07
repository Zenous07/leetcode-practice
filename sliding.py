def sliding(arr,target):
    count=0
    l=0
    r=1
    while l<r:
        sum=arr[l]
        if sum>=target:
            count=count+1
            l=l+1
        else:
            r=r+1
    print(count)



sliding([1,2,3],4)