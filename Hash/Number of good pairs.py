# https://leetcode.com/problems/number-of-good-pairs/description/?envType=problem-list-v2&envId=hash-table
# n*(n-1)/2 is used for calculating the number of unique possible combination of a number
def sol(nums):
    res = 0
    for i in set(nums):
        counts = nums.count(i)
        if counts > 1:
            res += counts*(counts-1)//2
    return res


print(sol([1, 2, 3, 1, 1, 3]))
print(sol([1, 2, 3]))
print(sol([1, 1, 1, 1]))
