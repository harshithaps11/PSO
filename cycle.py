class ListNode:
     def __init__(self, val):
         self.val = val
         self.next = None
def hasCycle(head):
    slow = head
    fast = head
    while ( fast is not None and fast.next is not None):
        slow = slow.next 
        fast = fast.next.next
        if (slow == fast):
            return True
    return False
n1,n2,n3,n4 = ListNode(3),ListNode(2),ListNode(0),ListNode(4)
n1.next,n2.next,n3.next,n4.next = n2,n3,n4,n2
print(hasCycle(n1))

