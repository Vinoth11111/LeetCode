# https://leetcode.com/problems/task-scheduler/description/
from collections import Counter, deque
import heapq
def sol(tasks, n):
    has = Counter(tasks)
    maxHeap = [-cnt for cnt in has.values()]
    heapq.heapify(maxHeap)
    q = deque()  # (cnt, time)
    time = 0
    while maxHeap or q:
        time += 1
        if maxHeap:
            cnt = 1 + heapq.heappop(maxHeap)  # since we use -cnt
            if cnt:
                q.append((cnt, time + n))  # next valid time to push back to heap
        if q and q[0][1] == time:
            heapq.heappush(maxHeap, q.popleft()[0])
    return time


print(sol(["A","A","A","B","B","B"], 2))  # 8
print(sol(["A","A","A","B","B","B"], 0))  # 6

