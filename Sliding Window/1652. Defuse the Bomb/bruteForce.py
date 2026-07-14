def defuse(code,k):
    n=len(code)
    if k==0:
        return [0]*n
    result=[0]*n
    print(sum(code[1%n:(k+1)%n]))
    for i in range(n):
        if k>0:
            for j in range(k):
                result[i]+=code[((i+j+1)%n)]
        else:
            for j in range(abs(k)):
                result[i]+=code[((i-j-1)%n)]
    return result
    

print(defuse([5,7],-2))
