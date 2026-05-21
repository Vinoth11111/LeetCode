# https://leetcode.com/problems/swap-nodes-in-pairs/description/

def sol(head):
    dummy = ListNode(0,head)

    tail = dummy
    curr = head
    while curr and curr.next:
        first = curr
        second = curr.next

        first.next = second.next
        second.next = first
        tail.next = second
        tail = first
        curr = first.next
    return dummy.next