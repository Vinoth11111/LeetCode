# https://leetcode.com/problems/unique-number-of-occurrences/?envType=study-plan-v2&envId=leetcode-75

def sol(arr):
    val = []
    for i in set(arr):
        count = arr.count(i)
        if count in val:
            return False
        else:
            val.append(count)

    return True


print(sol([1, 2, 2, 1, 1, 3]))
print(sol([1, 2]))


# solution 2
from collections import defaultdict


def sol1(arr):
    occ = defaultdict(int)
    for i in arr:
        occ[i] += 1
    val = set(occ.values())
    print(occ)
    return len(occ) == len(val)


print(sol1([1, 2, 2, 1, 1, 3]))
print(sol1([1, 2]))
