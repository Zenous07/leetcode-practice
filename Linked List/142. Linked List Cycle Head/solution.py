def linkedListStart(head):
    slow=head
    fast=head
    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            slow=head
            while slow!=fast:
                slow=slow.next
                fast=fast.next
            return slow
    return None