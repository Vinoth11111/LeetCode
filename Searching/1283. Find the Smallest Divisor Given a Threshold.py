# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/

from math import ceil

def sol(nums, threshold):
    left = 1
    right = max(nums)
    while left < right:
        mid = (left + right) // 2
        total = 0
        for num in nums:
            total += ceil(num / mid)
        if total > threshold:
            left = mid + 1
        else:
            right = mid
    return left


print(sol(nums=[1,2,5,9], threshold=6)) # 5
print(sol([44,22,33,11,1], 5)) # 44
