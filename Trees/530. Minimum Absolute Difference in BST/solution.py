def minAbsDiff(root):
    prev = None
    minV = float('inf')
    
    def inOrder(node):
        nonlocal prev, minV
        if not node:
            return
            
        inOrder(node.left)
        
        if prev is not None:
            minV = min(minV, node.val - prev.val)
        prev = node
        
        inOrder(node.right)
        
    inOrder(root)
    return minV