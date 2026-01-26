def baseball(operations):
    result=[]
    answer=0
    for i in range(0,len(operations)):
        if operations[i]=="+":
            temp1=result[-1]
            temp2=result[-2]
            temp1=int(temp1)
            temp2=int(temp2)
            result.append(temp1+temp2)
            answer+=temp1+temp2
        elif operations[i]=="D":
            temp=result[-1]
            temp=int(temp)
            result.append(temp*2)
            answer+=temp*2
        elif operations[i]=="C":
            temp=result.pop()
            temp=int(temp)
            answer-=temp
        else:
            temp=operations[i]
            temp=int(temp)
            result.append(temp)
            answer+=temp
    return answer

print(baseball(["5","2","C","D","+"]))
