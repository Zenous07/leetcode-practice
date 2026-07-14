def defuse(code,k):
    n=len(code)
    if k==0:
        return [0]*n
    
    result=[]
    extend=code+code
    totalSum=0

    if k>0:
        totalSum=sum(extend[1:k+1])
        result.append(totalSum)
    if k<0:
        totalSum=sum(extend[n+k:n])
        print(totalSum)
        result.append(totalSum)

    for r in range(1,n):
        if k>0:
            totalSum-=code[r]
            totalSum+=code[(r+k)%n]
            result.append(totalSum)
        else:
            totalSum-=code[(r+k-1)%n]
            totalSum+=code[r-1]
            result.append(totalSum)
    return result

print(defuse([5,7],-2))