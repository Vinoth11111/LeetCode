# https://leetcode.com/problems/find-peak-element/description/
"""
peak element is an element that is greater than its neighbors.
if the mid is smaller than its next element, then the peak must be in the right half, 
move right side
otherwise it is in the left half.
return the left pointer, which is the index of the peak element.
"""
def sol(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right)// 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


print(sol([1, 2, 3, 1]))
print(sol([1, 2, 1, 3, 5, 6, 4]))
