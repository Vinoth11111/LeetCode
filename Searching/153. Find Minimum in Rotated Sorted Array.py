# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

def sol(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left] 


print(sol([4, 5, 6, 7, 8, 9, 0, 1, 2, 3]))
print(sol([3,4,5,1,2]))
