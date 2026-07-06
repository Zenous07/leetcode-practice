def findMissingRepeatingNumbers(nums):
    result=[0,0]
    s=set()
    for i in range(1,len(nums)+1):
        s.add(i)

    for i in nums:
        if i in s:
            s.remove(i)
        else:
            result[0]=i
    result[1]=s.pop()

    return result

print(findMissingRepeatingNumbers([1, 2, 3, 6, 7, 5, 7]))