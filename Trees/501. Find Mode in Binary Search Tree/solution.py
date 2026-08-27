def findMode(root):
    if not root:
        return False
    result=[]
    def inOrder(node,result):
        if not node:
            return None
        else:
            inOrder(node.left,result)
            result.append(node.val)
            inOrder(node.right,result)
    inOrder(root,result)
    if len(result)==1:
        return result
    count=dict()
    for i in result:
        if i not in count:
            count[i]=1
        else:
            count[i]+=1
    stk=[]
    op=[]
    for item in count.items():
        if not stk:
            stk.append(item)
        elif stk[0][1]==item[1]:
            stk.append(item)
        elif stk[0][1]<item[1]:
            while stk:
                stk.pop()
            stk.append(item)
    for i in stk:
        op.append(i[0])
    return op