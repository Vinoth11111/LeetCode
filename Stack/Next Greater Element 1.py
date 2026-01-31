# https://leetcode.com/problems/next-greater-element-i/?envType=problem-list-v2&envId=array
def sol(num1, num2):
    stack = []
    has = {}

    for i in num2:
        while stack and stack[-1] < i:
            has[stack.pop()] = i
        stack.append(i)
    res = []
    for i in num1:
        res.append(has.get(i, -1))
    return res


print(sol([4, 1, 2], [1, 3, 4, 2]))
print(sol([2, 4], [1, 2, 3, 4]))
