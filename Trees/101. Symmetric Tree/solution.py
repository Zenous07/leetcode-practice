def symmetricTree(root):
    if not root:
        return True 
    lq=[root]
    rq=[root]
    while lq and rq:
        node1=lq.pop(0)
        node2=rq.pop(0)
        if node1.val != node2.val:
            return False
        if (node1.left and not node2.right) or (node2.right and not node1.left):
            return False
        if node1.left and node2.right:
            lq.append(node1.left)
            rq.append(node2.right)
        if (node1.right and not node2.left) or (node2.left and not node1.right):
            return False
        if node1.right and node2.left:
            lq.append(node1.right)
            rq.append(node2.left)
        
    if not lq and not rq:
        return True
    return False