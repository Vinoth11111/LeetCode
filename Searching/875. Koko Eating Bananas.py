# https://leetcode.com/problems/koko-eating-bananas/description/
from math import ceil
"""
find the bound left = 1 and right = max(piles) because the minimum speed is 1 and the maximum speed is the maximum pile.
find the mid
calculate the hours needed to eat all the piles with speed mid. divide the pile by mid and round up to get the hours.
if hours <= h we can try to decrease the speed by moving the right pointer to mid.
Time complexity is O(n log(m)) where n is the number of piles
Space complexity is O(1) because we are using constant space.
"""

def sol(piles, h):
    left = 1
    right = max(piles)
    while left <= right:
        mid = (left + right) // 2
        hours = 0
        for pile in piles:
            #hours += (pile + mid - 1) // mid # this is a trick to calculate the number of hours needed to eat the pile with speed mid.
            hours += ceil(pile / mid)
        if hours > h:
            left = mid + 1
        else:
            right = mid - 1
    return left

print(sol(piles=[3,6,7,11], h=8)) # 4
print(sol(piles=[30,11,23,4,20], h=5)) # 30