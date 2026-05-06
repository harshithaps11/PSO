class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

def rotateRight(head, k):
    if not head:
        return head

    # Step 1: store values in list
    arr = []
    curr = head
    while curr:
        arr.append(curr.val)
        curr = curr.next

    n = len(arr)

    # Step 2: rotate list
    k = k % n
    arr = arr[-k:] + arr[:-k]

    # Step 3: rebuild linked list
    new_head = ListNode(arr[0])
    curr = new_head
    for i in range(1, n):
        curr.next = ListNode(arr[i])
        curr = curr.next

    return new_head


# -------- MAIN --------
values = list(map(int, input("Enter values: ").split()))
k = int(input("Enter k: "))



# rotate
new_head = rotateRight(head, k)

# print
while new_head:
    print(new_head.val, end=" ")
    new_head = new_head.next