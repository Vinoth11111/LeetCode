# https://leetcode.com/problems/minimum-size-subarray-sum/
# follow up solve it in 0(nlog(n)) -> prefix 0(n) + binary search o(n(log(n)))
def sol(nums, target):
    if sum(nums) < target:
        return 0
    min_len = float('inf')
    left = 0
    curr_sum = 0
    for right in range(len(nums)):
        curr_sum += nums[right]
        while curr_sum >= target:
            min_len = min(min_len, right - left + 1)
            curr_sum -= nums[left]
            left += 1
    return min_len


print(sol([12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12], 213))
print(sol([2, 3, 1, 2, 4, 3], 7))
print(sol([1, 4, 4], 4))
print(sol([1, 1, 1, 1, 1, 1, 1, 1], 11))

