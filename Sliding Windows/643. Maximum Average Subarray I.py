# https://leetcode.com/problems/maximum-average-subarray-i/description/

def sol(nums, k):
    total_sum = sum(nums[:k])
    max_avg = total_sum / k

    left = 0

    for right in range(k, len(nums)):
        total_sum += nums[right] - nums[left]
        max_avg = max(max_avg, total_sum / k)
        left += 1

    return max_avg


print(sol([1, 12, -5, -6, 50, 3], 4))
print(sol([5], 1))
