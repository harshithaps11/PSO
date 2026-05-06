class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

# create list: 1->2->3->4->5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

def reverseList(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next   # save next
        curr.next = prev        # reverse link
        prev = curr             # move prev
        curr = next_node        # move curr

    return prev

# reverse
new_head = reverseList(head)

# print
curr = new_head
while curr:
    print(curr.val, end=" ")
    curr = curr.next