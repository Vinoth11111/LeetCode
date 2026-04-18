# https://leetcode.com/problems/sqrtx/
"""
we implement binary search to find the largest integer whose square is less than or equal to x.
1. We initialize two pointers, left and right, to define the search space. left starts at 0 and right starts at x.
2. We calculate the midpoint of the current search space and check if its square is equal to x
3. If the square of the midpoint is equal to x, we have found our answer and return the midpoint.
4. If the square of the midpoint is less than x, it means that the integer square root must be greater than the midpoint, so we move the left pointer to mid + 1.
5. If the square of the midpoint is greater than x, it means that the integer square root must be less than the midpoint, so we move the right pointer to mid - 1.
6. since we want large number we return right. 
"""


def sol(x):
    if x ==1:
        return 1
    left = 0
    right = x
    while left <= right:
        mid = (left+right)//2
        squared = mid * mid
        if squared == x:
            return mid
        elif squared < x:
            left = mid + 1
        else:
            right = mid -1
    return right

print(sol(4))
print(sol(2147395599))