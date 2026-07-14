def defuse(code,k):
    if k==0:
        return [0]*len(code)
    result=[0]*len(code)
    for i in range(len(code)):
        if k>0:
            for j in range(k):
                
                result[i]+=code[j]
        else:
            for j in range(k):
                result[i]+=code[j]
    return result

print(defuse([5,7,1,4],3))
