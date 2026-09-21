def merge(root1,root2):
    if not root1 and not root2:
        return []
    q1=[]
    q2=[]
    q3=[]
    temp=0
    if root1:
        q1.append(root1)
        temp+=root1.val
    if root2:
        q2.append(root2)
        temp+=root2.val
    root3=TreeNode(temp)
    q3.append(root3)
    while q1 or q2:
        node1=None
        node2=None
        if q1:
            node1=q1.pop(0)
        if q2:
            node2=q2.pop(0)
        parent=q3.pop(0)
        if node1 and node2 and node1.left and node2.left:
            q1.append(node1.left)
            q2.append(node2.left)
            parent.left=TreeNode(node1.left.val+node2.left.val)
            q3.append(parent.left)
        elif node1 and node1.left:
            q1.append(node1.left)
            parent.left=TreeNode(node1.left.val)
            q3.append(parent.left)
        elif node2 and node2.left:
            q2.append(node2.left)
            parent.left=TreeNode(node2.left.val)
            q3.append(parent.left)
        else:
            parent.left=None

        if node1 and node2 and node1.right and node2.right:
            q1.append(node1.right)
            q2.append(node2.right)
            parent.right=TreeNode(node1.right.val+node2.right.val)
            q3.append(parent.right)
        elif node1 and node1.right:
            q1.append(node1.right)
            parent.right=TreeNode(node1.right.val)
            q3.append(parent.right)
        elif node2 and node2.right:
            q2.append(node2.right)
            parent.right=TreeNode(node2.right.val)
            q3.append(parent.right)
        else:
            parent.right=None
    return root3