def pathSum(root,targetSum):
    if not root:
        return False
    stk=[(root,root.val)]
    while stk:
        node,curr_sum=stk.pop()
        if node.right:
            stk.append((node.right,curr_sum+node.right.val))
        if node.left:
            stk.append((node.left,curr_sum+node.left.val))
        if not node.left and not node.right:
            if curr_sum==targetSum:
                return True
    return False