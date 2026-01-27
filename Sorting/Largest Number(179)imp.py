# https://leetcode.com/problems/largest-number/description/
from functools import cmp_to_key


def sol(nums) -> str:
    str_num = list(map(str, nums))

    def check(a, b):
        if a + b > b + a:  # if A is high no swaping
            return -1
        elif a + b < b + a:  # if b produce high value swap
            return 1
        else:  # if both value same.remain same no swaping
            return 0
    str_num.sort(key=cmp_to_key(check))  # by default sort only sort by order not by condition
    # in order for comparison based sorting we have cmp_to_map function from function tools.
    # it returns -1,1,0 if 1 swap else no swaping.

    if str_num[0] == '0':  # basecase if we have multiple 0 return 0
        return '0'
    return ''.join(str_num)


def sol1(nums):
    str_num = list(map(str, nums))
    str_num.sort(key=lambda x: x*10, reverse=True)
    if str_num[0] == '0':
        return 0
    return ''.join(str_num)


print(sol([10, 2]))
print(sol([3, 30, 34, 5, 9]))
print(sol([0, 0, 0, 0]))
print(sol1([10, 2]))
print(sol1([3, 30, 34, 5, 9]))
print(sol1([0, 0, 0, 0]))
