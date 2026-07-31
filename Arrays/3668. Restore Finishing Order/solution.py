def restoreOrder(order,friends):
    s=set(friends)
    result=[]
    for i in order:
        if i in s:
            result.append(i)
    return result

print(restoreOrder([3,1,2,5,4],[1,3,4]))