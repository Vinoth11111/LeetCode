# https://leetcode.com/problems/longest-consecutive-sequence/
def sol(nums):
    long_count = 0
    for i in nums:
        if i-1 not in nums: # avoid rechecking to achieve o(n)
            cnt = 1
            seen = i+1
            while seen in nums:
                cnt += 1
                seen += 1
            long_count = max(long_count, cnt)
    return long_count


print(sol([100, 4, 200, 1, 3, 2]))
print(sol([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(sol([1, 0, 1, 2]))
