def uniqueOccurrences(arr):
    d=dict()
    s=set()
    for i in range(len(arr)):
        if arr[i] in d:
            d[arr[i]]+=1
        else:
            d[arr[i]]=0

    for val in d.values():
        if val in s:
            return False
        else:
            s.add(val)
    return True

print(uniqueOccurrences([1,2,2,1,1,3]))