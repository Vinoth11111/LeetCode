"""
find the minimum peek and find the amount water it can hold at that peek.
make sure to minus the current height with the minumum peak because thats the maximum water it can hold at that peek.
Time complexity is O(n) because we are iterating through the array once
Space complexity is O(1) because we are using constant space
"""
def sol(height):
    left = 0
    right = len(height) - 1
    left_max = height[left]
    right_max = height[right]
    res = 0

    while left < right:
        # if the left peek is smaller, which means no mater how big the right peek is, 
        # the water can only be hold by the left peek
        if height[left] < height[right]:
            left += 1
            left_max = max(left_max, height[left])
            res += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            res += right_max - height[right]
    return res