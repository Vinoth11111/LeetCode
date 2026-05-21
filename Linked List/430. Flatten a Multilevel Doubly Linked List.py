# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def sol(head):
    if not head:
        return None
    
    curr = head
    while curr:
        if curr.child:
            next_node = curr.next
            last_child = curr.child
            while last_child.next:
                last_child = last_child.next
            last_child.next = next_node
            next_node.prev = last_child
            curr.next = curr.child
            curr.child.prev = curr
            curr.child = None
        curr = curr.next
    return head
            