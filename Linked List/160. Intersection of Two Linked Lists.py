# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
def sol(node1, node2):
    a = node1
    b = node2

    seen = set()
    while a:
        seen.add(a)
        a = a.next
    while b:
        if b in seen:
            return b
        b = b.next
    return None


def sol1(node1, node2):
    a = node1
    b = node2
    while a is not b:
        a = a.next if a else node2
        b = b.next if b else node1
    return a


print(sol([4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5]))
print(sol1([4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5]))
