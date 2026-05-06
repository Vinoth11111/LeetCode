# https://leetcode.com/problems/single-element-in-a-sorted-array/description/


def sol(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if (mid % 2 == 0) and nums[mid] == nums[mid-1] or (mid % 2 == 1) and (nums[mid] == nums[mid+1]):
            right = mid
        else:
            left = mid + 1
    return nums[left]

#          0,1,2,3,4,5,6,7,8
print(sol([1,1,2,3,3,4,4,8,8])) # 2
#          0,1,2,3,4,5,6,7
print(sol([3,3,7,7,10,11,11])) # 10
