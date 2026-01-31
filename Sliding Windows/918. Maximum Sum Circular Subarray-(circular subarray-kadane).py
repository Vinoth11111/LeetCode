# https://leetcode.com/problems/maximum-sum-circular-subarray/description/
def sol(nums):
    cur = 0
    max_ans = float('-inf')
    for i in range(len(nums)):
        cur = max(nums[i], nums[i] + cur)
        max_ans = max(max_ans, cur)
    if max_ans < 0:
        return max_ans
    total_sum = sum(nums)

    min_ans = float('inf')
    cur_min = 0
    for i in range(len(nums)):
        cur_min = min(nums[i], cur_min + nums[i])
        min_ans = min(min_ans, cur_min)
    circular_max = total_sum - min_ans
    return max(max_ans, circular_max)


print(sol([1, -2, 3, -2]))
print(sol([5, -3, 5]))
print(sol([-3, -2, -3]))
