"""
we can use 2 pointers to solve this problem
since the is monotonic.
we can compare the left and right pointer and find the bigger one and add it to the result array
if left pointer is bigger we add it to the end of the result and move left pointer to the right
if right pointer is bigger we add it to the end of the result and move right pointer to the left
Time complexity is O(n) because we are iterating through the array once
Space complexity is O(n) because we are using an extra array to store the result
"""

def sol(nums: list[int]) -> list[int]:
    # return sorted([num**2 for num in nums])
    n = len(nums)
    result = [0] * n
    left = 0
    right = n-1
    while left <= right:
        n-= 1
        if abs(nums[left]) > abs(nums[right]):
            result[n] = nums[left] * nums[left]
            left += 1
        else:
            result[n] = nums[right] * nums[right]
            right -= 1
    return result


print(sol([-4, -1, 0, 3, 10]))  # [0, 1, 9, 16, 100]
print(sol([-7, -3, 2, 3, 11]))  # [4, 9, 9, 49, 121]
