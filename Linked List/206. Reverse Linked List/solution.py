def reverse(head):
    curr=head
    prev=None
    while curr !=None:
        temp=curr.next
        curr.next=prev
        prev=curr
        curr=temp

    return prev