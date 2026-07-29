def Fibo(n):
    if n==0:
        return 0
    if n<=2:
        return 1
    series=[0]*(n+1)
    series[0]=0
    series[1]=1
    for i in range(2,n+1):
        series[i]=series[i-1]+series[i-2]
    return series[n]

print(Fibo(7))