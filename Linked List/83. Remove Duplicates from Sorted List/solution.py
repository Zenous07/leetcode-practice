# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def removeDepulicate(self,head):
    if head==None:return head
    curr=head
    while curr!=None and curr.next != None:
        while curr.next!=None and curr.val==curr.next.val:
            if curr.next.next !=None:
                curr.next=curr.next.next
            else:
                curr.next=None
        curr=curr.next
    return head
    