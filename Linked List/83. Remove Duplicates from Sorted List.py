# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sol(head):
    seen = set()
    h = head
    dummy = ListNode()
    tail = dummy
    while h:
        if h.val not in seen:
            seen.add(h.val)
            tail.next = h
            tail = tail.next
        h = h.next

    tail.next = None
    return dummy.next


print(sol([1, 1, 2]))
