def invertTree(root):
    if not root:
        return root
    q=[]
    q.append(root)
    while q:
        node=q.pop(0)
        node.left,node.right=node.right,node.left
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    
    return root