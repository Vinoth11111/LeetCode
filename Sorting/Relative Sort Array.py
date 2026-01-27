# https://leetcode.com/problems/relative-sort-array/description/
from collections import Counter


def sol(arr1, arr2):
    res = []
    has = Counter(arr1)

    for i in arr2:
        res.extend([i] * has[i])
        del has[i]

    for i in sorted(has):
        res.extend([i] * has[i])

    return res


def sol1(arr1, arr2):
    counts = {val: i for i, val in enumerate(arr2)}
    arr1.sort(key=lambda x: (counts.get(x, len(arr2) + x)))
    return arr1


print(sol([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]))
print(sol([28, 6, 22, 8, 44, 17], [22, 28, 8, 6]))
print(sol1([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]))
print(sol1([28, 6, 22, 8, 44, 17], [22, 28, 8, 6]))
