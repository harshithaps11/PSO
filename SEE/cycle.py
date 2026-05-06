class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

# create list: 3->2->0->-4 and make cycle
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)

# create cycle (last node points to node with value 2)
head.next.next.next.next = head.next


def hasCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


print(hasCycle(head))  # True