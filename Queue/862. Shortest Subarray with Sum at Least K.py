# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/

# find the shortest subarray with sum at least k
# use prefix sum and monotonic queue(increasing)
# for finding the subarry with sum at least k, curr_sum - subarray_start_sum >= k
# find the min subaary. curr_idx - subarray_start_index
# if the current index is smaller than the last one in the queue, pop the last one since it won't be the answer
from collections import deque
def sol(nums, k):
    q = deque()
    n = len(nums)
    prefix = [0] * (n + 1)
    res = float('inf')

    # creating the prefix sum array
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]
    
    # creating the monotonic queue
    for i in range(n + 1):
        while q and prefix[i] - prefix[q[0]] >= k:
            res = min(res, i - q.popleft())
        while q and prefix[i] <= prefix[q[-1]]:
            q.pop()
        q.append(i)
    return res if res != float('inf') else -1


print(sol([1], 1))  # 1
print(sol([1, 2], 4))  # -1
print(sol([2, -1, 2], 3))  # 3
