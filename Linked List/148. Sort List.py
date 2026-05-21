# https://leetcode.com/problems/sort-list/description/

from xarray import merge

"time complexity: O(n log n), space complexity: O(1) if we don't consider the recursive stack space, otherwise O(log n) due to recursion"
def sol1(head):
    if not head or not head.next:
        return head

    values = []
    curr = head
    while curr:
        values.append(curr.val)
        curr = curr.next
    values.sort()

    node = head
    i = 0
    while node:
        node.val = values[i]
        node = node.next
        i += 1
    return head


def sol(head):
    if not head or not head.next:
        return head

    # Split the list into halves
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    # Sort each half
    left = sol(head)
    right = sol(mid)

    # Merge sorted halves
    return merge(left, right)


print(sol([4, 2, 1, 3]))
print(sol([-1, 5, 3, 4, 0]))
