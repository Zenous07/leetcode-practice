def kthFactor(n,k):
    fact=[]
    for i in range(1,n+1):
        if n%i==0:
            fact.append(i)
    if len(fact)<k:
        return -1
    return fact[k-1]

print(kthFactor(12,3))