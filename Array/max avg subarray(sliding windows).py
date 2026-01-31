def slide_windows(nums, k):
    total_sum = sum(nums[:k])
    max_avg = total_sum/k
    for i in range(k, len(nums)):
        total_sum += nums[i] - nums[i-k]
        max_avg = max(max_avg, total_sum/k)
    return max_avg


print(slide_windows([1, 12, -5, -6, 50, 3], 4))
print(slide_windows([5], 1))
# https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75
