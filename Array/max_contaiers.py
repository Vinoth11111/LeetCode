#https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=leetcode-75
def water_hold(height):
    n = len(height)
    left = 0
    right = n-1
    res = 0
    while left < right:
        leng = right-left
        high = min(height[left],height[right])
        res = max(res,leng*high)
    return res


height = []
print(water_hold(height))
