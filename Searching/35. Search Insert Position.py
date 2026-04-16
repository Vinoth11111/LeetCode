# https://leetcode.com/problems/search-insert-position/description/
"""
for this problem we can use binary search to find the target in the array.
if we find the target we return the index of the target.
if we don't find the target we return the index where the target should be inserted in order to maintain the sorted order of the array.
we can use the left pointer to find the index.
Time complexity is O(log(n)) because we are using binary search.
Space complexity is O(1) because we are using constant space.
"""

def sol(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) //2
        if nums[mid] == target:
            return mid
        elif nums[mid]  < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
