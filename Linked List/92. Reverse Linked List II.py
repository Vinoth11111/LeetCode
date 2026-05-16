# https://leetcode.com/problems/reverse-linked-list-ii/description/

def sol(head, left, right):

    dummy = ListNode(0,head)
    prev = dummy

    # left
    for _ in range(left - 1):
        prev = prev.next
    
    rev_list = None
    cur = prev.next

    # reversed
    for _ in range(right - left + 1):
        next_val = cur.next
        cur.next = rev_list
        rev_list = cur
        cur = next_val

    # right
    tail = prev.next
    prev.next = rev_list
    tail.next = cur
    return dummy.next



