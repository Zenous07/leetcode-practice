def BTLevelOrderTraversal(root):
    if not root:
        return []
    result=[]
    q=[root]
    while q:
        level_size=len(q)
        temp=[]
        for _ in range(level_size):
            node=q.pop(0)
            temp.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(temp)
    return result