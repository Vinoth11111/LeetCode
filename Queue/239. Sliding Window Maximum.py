# https://leetcode.com/problems/sliding-window-maximum/
from collections import deque


def sol(nums, k):
    q = deque()
    res = []
    for i in range(len(nums)):
        if i <= i-k:  # detect the max window
            q.popleft()

        while q and nums[q[-1]] < nums[i]:  # remove the last value if its smaller than curr(monotonic increasing)
            q.pop()
        q.append(i)
        if i >= k-1:  # only find the max values after the k values(initial)
            res.append(nums[q[0]])
    return res


print(sol([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(sol([1], 1))
