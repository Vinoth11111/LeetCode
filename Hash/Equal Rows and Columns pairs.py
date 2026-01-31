# https://leetcode.com/problems/equal-row-and-column-pairs/?envType=study-plan-v2&envId=leetcode-75
from collections import Counter


def sol(grid):
    res = 0
    row = Counter(tuple(row) for row in grid)

    for col in zip(*grid):
        res += row[col]
    return res


print(sol([[3, 2, 1],[1, 7, 6],[2, 7, 7]]))
