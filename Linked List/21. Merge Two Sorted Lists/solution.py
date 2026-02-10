# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def merge(list1,list2):
    dummy=ListNode(0)
    curr=dummy
    curr1=list1
    curr2=list2
    while curr1 !=None and curr2 !=None:
        if curr1.val <= curr2.val:
            curr.next=curr1
            curr=curr.next
            curr1=curr1.next
        else:
            curr.next=curr2
            curr=curr.next
            curr2=curr2.next
    if curr1 == None:
        while curr2 != None:
            curr.next=curr2
            curr=curr.next
            curr2=curr2.next
    if curr2 ==None:
        while curr1!=None:
            curr.next=curr1
            curr=curr.next
            curr1=curr1.next
    return dummy.next