def temperat(temperatures):
    length=len(temperatures)
    result=[0]*length
    stck=[]
    stck.append([temperatures[0],0])
    for i in range(1,length):
        if stck[-1][0]>temperatures[i]:
            stck.append([temperatures[i],i])
        else:
            while len(stck)>0 and stck[-1][0]<temperatures[i]:
                temps=stck.pop()
                result[temps[-1]]=i-temps[-1]
            stck.append([temperatures[i],i])
    return result

print(temperat([73,74,75,71,69,72,76,73])),