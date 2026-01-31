# https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75

"""a = [1,2,3,4]
k = 5
counts = 0
for i in a:
    for j in a:
        if i+j == k:
            counts +=1
            a.remove(i)
            a.remove(j)

print(counts)"""

from collections import Counter


def check(nums,k):
    counts = Counter(nums)
    ope = 0
    for i in counts:
        com = k-i
        if com in counts:
            if com == i:
                ope += counts[i]//2
            else:
                pairs = min(counts[i], counts[com])
                ope += pairs
                counts[i] -= pairs
                counts[com] -= pairs

    return ope


print(check([1,2,3,4],5))
