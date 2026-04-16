# https://leetcode.com/problems/binary-search/
"""
we have solve this problem in O(log(n)) time complexity using binary search.
we have two pointers left and right that point to the start and end of the array.
we find the mid index and check if the mid element is equal to the target or not.
if mid element is equal to the target we return the mid index.
if mid element is less than the target we move the left pointer to mid + 1.
if mid element is greater than the target we move the right pointer to mid - 1.
if left and right pointers meet then we have no target in the array and we return -1.
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
    return -1


print(sol([-1,0,3,5,9,12], 9)) # 4
print(sol([-1,0,3,5,9,12], 2)) # -1
