# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

# method 1: hash map

def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement] + 1, i + 1]
        num_map[num] = i


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([2, 3, 4], 6))


# method 2: binary search

def twoSum(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

print(twoSum([2, 7, 11, 15], 9))
print(twoSum([2, 3, 4], 6))
