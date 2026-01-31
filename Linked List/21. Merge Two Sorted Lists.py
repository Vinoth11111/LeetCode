# https://leetcode.com/problems/merge-two-sorted-lists/

class LinkedNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(list):
    dummy = LinkedNode()
    tail = dummy
    for i in list:
        tail.next = LinkedNode(i)
        tail = tail.next
    return dummy.next


def sol(list1, list2):
    dummy = LinkedNode()
    tail = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    if list2:
        tail.next = list2
    return dummy.next


res = sol(build_linked_list([1, 2, 4]), build_linked_list([1, 3, 4]))

val = ''
while res:
    val += str(res.val) + '->'
    res = res.next
print(val)