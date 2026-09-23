def addTwoNumbers(l1,l2):
    dummy=ListNode()
    temp=dummy
    curr1=l1
    curr2=l2
    sum1=''
    sum2=''
    while curr1:
        sum1+=str(curr1.val)
        curr1=curr1.next
    while curr2:
        sum2+=str(curr2.val)
        curr2=curr2.next
    if sum1=='':
        sum1=0
    if sum2 == '':
        sum2=0
    sum1=int(sum1[::-1])
    sum2=int(sum2[::-1])
    res=(sum1+sum2)
    while res:
        last=res%10
        dummy.val=last
        res=res//10
        if res:
            dummy.next=ListNode()
            dummy=dummy.next
    return temp
    