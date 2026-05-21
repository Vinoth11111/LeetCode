# https://leetcode.com/problems/copy-list-with-random-pointer/description/

from attr import has
from httpx import head


class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def sol(head):
    has = {}
    curr = head
    if not head:
        return None
    while curr:
        has[curr] = Node(x = curr.val)
        curr = curr.next

    sub = head

    while sub:
        has[sub].next = has.get(sub.next)
        has[sub].random = has.get(sub.random)
        sub = sub.next
    return has[head]


print(sol([[7,'null'],[13,0],[11,4],[10,2],[1,0]]))
"""
new_list = Node(0)
list1 = list(range(1, 5))
print(list1)
tail = new_list
for i in list1:
    tail.next = Node(i)
    tail = tail.next
curr = new_list.next
res = ''
while curr:
    res += str(curr.val) + '->'
    curr = curr.next
print(res)"""