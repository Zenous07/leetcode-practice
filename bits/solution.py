def hammingDistance(x,y):
    result=bin(x^y)
    count=0
    for i in range(0,len(result)):
        if result[i]=='1':
            count+=1
    return count

print(hammingDistance(3,7))