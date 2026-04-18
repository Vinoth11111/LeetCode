# https://leetcode.com/problems/peak-index-in-a-mountain-array/
"""
here we want to find the peak index in the array.
since we want to account mid we are using left < right and right = mid.
finally return the left or right since they are equal.
Time complexity is O(log(n)) because we are using binary search.
Space complexity is O(1) because we are using constant space.
"""
def sol(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left


print(sol([0,1,0])) # 1
print(sol([0,2,3,1,0])) # 1
