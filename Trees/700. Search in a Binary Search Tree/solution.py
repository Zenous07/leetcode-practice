def searchBST(root,val):
    def search(node,val):
        if not node:
            return True
        if node.val == val:
            return True
        if val>node.val:
            return search(node.right,val)
        elif val<node.val:
            return search(node.left,val)
        else:
            return False
    return search(root,val)