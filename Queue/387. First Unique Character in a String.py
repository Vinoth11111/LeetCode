# https://leetcode.com/problems/first-unique-character-in-a-string/description/
from collections import defaultdict, deque


def sol(s):
    has = defaultdict(int)
    q = deque()

    for i, val in enumerate(s):
        has[val] += 1

        if has[val] == 1:
            q.append(i)
        while q and has[s[q[0]]] > 1:
            q.popleft()
    return q[0] if q else  -1


print(sol("leetcode"))
print(sol("aabb"))
