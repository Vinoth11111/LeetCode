# https://leetcode.com/problems/number-of-recent-calls/
from collections import deque


class RecentCounter:
    def __init__(self):
        self.cnt = deque()

    def ping(self, t: int) -> int:
        val = t - 3000  # track previous time with t-3000 so see whether its in the bound or out.
        while self.cnt and self.cnt[0] < val:
            self.cnt.popleft()
        self.cnt.append(t)
        return len(self.cnt)


obj = RecentCounter()
print([obj.ping(i[0]) for i in [[1], [100], [3001], [3002]]])