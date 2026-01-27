# https://leetcode.com/problems/maximum-subarray/
def sol(nums):
    max_sum = nums[0]
    cur_sum = nums[0]
    # if curr_sum is negative we have to start a new curr_sum
    for i in range(1,len(nums)):
        cur_sum = max(nums[i], cur_sum+nums[i])
        max_sum = max(cur_sum, max_sum)
    return max_sum


print(sol([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(sol([1]))
