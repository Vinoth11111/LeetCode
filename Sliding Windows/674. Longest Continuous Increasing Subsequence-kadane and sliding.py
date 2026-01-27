# https://leetcode.com/problems/longest-continuous-increasing-subsequence/
def sol(nums):  # sliding window
    res = 0
    left = 0
    stack = []
    for i in range(len(nums)):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop(0)
            left += 1
        stack.append(i)
        res = max(res, i - left + 1)
    return res


def sol1(nums):  # kadane
    cur = 1
    res = 1
    for i in range(1, len(nums)):
        if nums[i-1] < nums[i]:
            cur += 1
        else:
            cur = 1
        res = max(res, cur)
    return res


print(sol([1, 3, 5, 4, 7]))
print(sol([2, 2, 2, 2, 2]))
print(sol1([1, 3, 5, 4, 7]))
print(sol1([2, 2, 2, 2, 2]))
