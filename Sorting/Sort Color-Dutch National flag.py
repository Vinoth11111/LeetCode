# https://leetcode.com/problems/sort-colors/description/
"""


"""
def sol(nums):
    low = 0
    mid = 0
    high = len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1
    return nums


print(sol([2, 0, 2, 1, 1, 0]))
print(sol([2, 0, 1]))
