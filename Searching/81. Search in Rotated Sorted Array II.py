# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

def sol(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right)//2
        if nums[mid] == target:
            return True
        elif nums[left] == nums[mid] == nums[right]:
            left += 1
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return False


print(sol([2,5,6,0,0,1,2], 0)) # True
print(sol([2,5,6,0,0,1,2], 3)) # False
