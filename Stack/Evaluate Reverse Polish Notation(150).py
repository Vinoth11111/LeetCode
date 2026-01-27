# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
def sol(tokens):
    stack = []
    for i in tokens:
        for i in tokens:
            if stack and i == '+':
                res = stack.pop(-2) + stack.pop(-1)
                stack.append(res)
            elif stack and i == '-':
                res = stack.pop(-2) - stack.pop(-1)
                stack.append(res)
            elif stack and i == '*':
                res = stack.pop(-2) * stack.pop(-1)
                stack.append(res)

            elif stack and i == '/':
                res = stack.pop(-2) / stack.pop(-1)
                stack.append(int(res))
            else:
                stack.append(int(i))
        return stack[0]


print(sol(["2", "1", "+", "3", "*"]))
print(sol(["4", "13", "5", "/", "+"]))
print(sol(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
