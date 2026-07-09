def validParanthese(s):
    d={'(':')','{':'}','[':']'}
    stk=[]
    for i in s:
        if i in d.keys():
            stk.append(i)
        else:
            if len(stk) <=0:
                return False
            if i != d[stk.pop()]:
                return False
    if stk:
        return False
    return True

print(validParanthese("()[]{}"))