# https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=study-plan-v2&envId=leetcode-75
def sol(nums1, nums2):
    has1 = {}
    has2 = {}
    res = [[], []]
    for i in set(nums1):
        if i not in has1:
            has1[i] = 1
    for j in set(nums2):
        if j not in has2:
            has2[j] = j
        if j not in has1:
            res[1].append(j)
    for i in has1:
        if i not in has2:
            res[0].append(i)
    return res


print(sol([1, 2, 3, 3], [1, 1, 2, 2]))
print(sol([1, 2, 3], [2, 4, 6]))

# solution2


def sol1(num1, num2):
    n1 = set(num1)
    n2 = set(num2)
    dif1 = [n1 - n2]
    dif2 = [n2 - n1]
    return [dif1, dif2]


print(sol1([1, 2, 3, 3], [1, 1, 2, 2]))
print(sol1([1, 2, 3], [2, 4, 6]))
