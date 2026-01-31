# https://leetcode.com/problems/linked-list-cycle/description/
# in this problem we randomly given circular list and linkedlist, if have to return True if we have circular list else False.
def sol(head):
    fast = head
    while fast and fast.next:
        head = head.next
        fast = fast.next.next

        if head is fast:
            return True
    return False


print(sol([3, 2, 0, -4]))
