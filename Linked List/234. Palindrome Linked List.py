# https://leetcode.com/problems/palindrome-linked-list/
def sol(head):
    vals = []
    h = head
    while h:
        vals.append(h.val)
        h = h.next
    return vals == vals[::-1]


print(sol([1, 2, 2, 1]))
