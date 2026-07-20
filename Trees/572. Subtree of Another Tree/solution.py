def isSubTree(root,subRoot):
    if not root and not subRoot:
        return True
    if not root or not subRoot:
        return False
    rq=[root]
    match=False
    while rq:
        noder=rq.pop(0)
        nodesr=subRoot
        if noder.val==nodesr.val:
            match=True
            irq=[noder]
            isrq=[nodesr]
            while irq and isrq and match:
                inoder=irq.pop(0)
                inodesr=isrq.pop(0)
                if inoder.val == inodesr.val:
                    if inoder.left and inodesr.left:
                        irq.append(inoder.left)
                        isrq.append(inodesr.left)
                    elif (inoder.left and not inodesr.left) or (inodesr.left and not inoder.left):
                        match=False
                    if inoder.right and inodesr.right:
                        irq.append(inoder.right)
                        isrq.append(inodesr.right)
                    elif (inoder.right and not inodesr.right) or (inodesr.right and not inoder.right):
                        match=False
                else:
                    match=False
            if not irq and not isrq and match:
                return True
            if noder.left:
                rq.append(noder.left)
            if noder.right:
                rq.append(noder.right)
        else:
            if noder.left:
                rq.append(noder.left)
            if noder.right:
                rq.append(noder.right)
    return False
