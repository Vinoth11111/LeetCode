# https://leetcode.com/problems/find-k-closest-elements/description/

"""
we have to find the starting element of the k closest to x, 
if we find the starting point of k then we can easly say the start + k 
determine the bounds
left = 0
right = len(arr) - k because we want to find the starting point of k elements, so the last starting point can be len(arr) - k

compare the x and mid ,
   * if x <= mid the staring on the left side
   * if x >= mid + k the staring on the right side
   * if we have a bound then find which one is closer to x and return the k elements starting from the closer one
"""

def sol(arr, k, x):
    left = 0
    right = len(arr) - k

    while left < right:
        mid = (left + right) // 2
        if x <= arr[mid]:
            right = mid
        elif x >= arr[mid + k]:
            left = mid + 1
        else:
            if x - arr[mid] <= arr[mid + k] - x:
                right = mid
            else:
                left = mid + 1
    return arr[left:left + k]
print(sol([1,2,3,4,5], 4, 3)) # [1,2,3,4]
print(sol(arr = [1,1,2,3,4,5], k = 4, x = -1)) # [1,1,2,3]
