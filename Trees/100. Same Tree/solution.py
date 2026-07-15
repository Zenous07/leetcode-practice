def sameTree(p,q):
    if not p and q:
        return False
    if not q and p:
        return False
    if not q and not p:
        return True
    pq=[p]
    qq=[q]
    while pq and qq:
        node1=pq.pop(0)
        node2=qq.pop(0)
        if node1.val != node2.val:
            return False
        if node1.left and node2.left: 
            pq.append(node1.left)
            qq.append(node2.left)
        if (node1.left and not node2.left) or (node2.left and not node1.left):
            return False
        if node1.right and node2.right:
            pq.append(node1.right)
            qq.append(node2.right)
        if (node1.right and not node2.right) or (node2.right and not node1.right):
            return False
    if not pq and not qq:
        return True

    return False