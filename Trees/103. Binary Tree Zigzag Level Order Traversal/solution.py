def zigzagLevelOrder(root):
    if not root:
        return []
    result=[]
    q=deque()
    q.append(root)
    idx=1
    while q:
        temp=[]
        len_q=len(q)
        for _ in range(len_q):
            node=q.popleft()
            temp.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        if idx % 2 !=0:
            result.append(temp)
            idx+=1
        else:
            result.append(temp[::-1])
            idx+=1
    return result