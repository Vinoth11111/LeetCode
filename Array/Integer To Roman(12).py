# https://leetcode.com/problems/integer-to-roman/description/?envType=problem-list-v2&envId=string
def sol(nums):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    res = ''
    for i in range(len(val)):
        while nums >= val[i]:
            res += syb[i]
            nums -= val[i]
    return res


print(sol(3749))
print(sol(1994))
