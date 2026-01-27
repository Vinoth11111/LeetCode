class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sol(head):
    odd = ListNode()
    even = ListNode()
    o_tail = odd
    e_tail = even
    count = 1
    h = head
    while h:
        if count % 2 != 0:
            o_tail.next = h
            o_tail = o_tail.next
        else:
            e_tail.next = h
            e_tail = e_tail.next
        h = h.next
        count += 1
    e_tail.next = None
    o_tail.next = even.next
    return odd.next


print(sol([1, 2, 3, 4, 5]))
