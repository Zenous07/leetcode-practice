def kthSmallest(root):
    result=[]
    def inOrder(node):
        if not node:
            return None
        else:
            inOrder(node.left)
            result.append(node.val)
            inOrder(node.right)
        inOrder(root)
    return result[k-1]
