# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
def build_list(vals):
    pass


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sol(head, n):
    dummy = ListNode(0, head)
    right = dummy
    left = dummy
    for _ in range(n):
        right = right.next
    while right.next:
        right = right.next
        left = left.next

    left.next = left.next.next

    return dummy.next


print(sol(build_list([1, 2, 3, 4, 5]), 2))
