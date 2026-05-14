# https://leetcode.com/problems/reverse-linked-list/description/

def sol(head):
    cur = head
    prev = None

    while cur:
        next_value = cur.next
        cur.next = prev
        prev = cur
        cur = next_value
    return prev


print(sol([1, 2, 3, 4, 5]))

