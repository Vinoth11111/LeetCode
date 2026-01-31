# https://leetcode.com/problems/middle-of-the-linked-list/description/
class LinkedNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def buildlist(val):
    element = LinkedNode()
    tail = element
    for i in val:
        tail.next = LinkedNode(i)
        tail = tail.next
    return element.next

# my sol
def sol(head):
    fast = head
    slow = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    if fast.next:
        slow = slow.next

    return slow.val

# optimal solution

def sol1(head):
    fast = head
    slow = head
    while fast.next and fast:
        slow = slow.next
        fast = fast.next.next
    return slow.val


print(sol(buildlist([1, 2, 3, 4, 5])))
print(sol1(buildlist([1, 2, 3, 4, 5])))
print(buildlist([1, 2, 3, 4, 5]))
