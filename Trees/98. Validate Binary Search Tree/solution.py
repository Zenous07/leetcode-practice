def validateBST(root):
    if not root:
        return True
    q=[root]
    while q:
        node=q.pop(0)
        if node.left:
            if node.val <= node.left.val:
                return False
            q.append(node.left)
        if node.right:
            if node.val >= node.right.val:
                return False
            q.append(node.right)
    if not q:
        return True