def minAbsDiff(root):
    if not root:
        return 0
    minDiff=0
    q=[root]
    while q:
        node = q.pop(0)
        if node.left:
            minDiff=min(minDiff,abs(node.val-node.left.val))
            q.append(node.left)
        if node.right:
            minDiff=min(minDiff,abs(node.val,node.right.val))
            q.append(node.right)
    return minDiff