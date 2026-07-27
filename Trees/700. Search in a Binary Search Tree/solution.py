def searchBST(root,val):
    def search(node,val):
        if node.val == val:
            return node
        if val>node.val and node.right:
            return search(node.right,val)
        elif val<node.val and node.left:
            return search(node.left,val)
        else:
            return None
    return search(root,val)