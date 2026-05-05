# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/

"""
min days required is min of bloomday
max days required is max of bloomday
find the mid and check if we can make m bouquets with k flowers in mid days
if we can make m bouquets with k flowers in mid days then we can try to find a smaller number of days by setting right to mid
if we cannot make m bouquets with k flowers in mid days then we need to increase the number of days by setting left to mid + 1
"""

def sol(bloomDay, m, k):
    if (m*k) > len(bloomDay):
        return -1
    left = min(bloomDay)
    right = max(bloomDay)
    while left < right:
        mid = (left + right) // 2

        total_flowers = 0
        bouquets = 0
        for day in bloomDay:
            if day <= mid:
                total_flowers += 1
                if total_flowers == k:
                    bouquets += 1
                    total_flowers = 0
            else:
                total_flowers = 0
        
        if bouquets >= m:
            right = mid
        else:
            left = mid + 1
    return left
    


print(sol(bloomDay=[1,10,3,10,2], m=3, k=1)) # 3
print(sol(bloomDay=[1,10,3,10,2], m=3, k=2)) # -1
