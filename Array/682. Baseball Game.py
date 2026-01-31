# https://leetcode.com/problems/baseball-game/description/?envType=problem-list-v2&envId=array
def sol(operations):
    stack = []
    for i in operations:
        if i == '+':
            stack.append(stack[-1] + stack[-2])
        elif i == 'C':
            stack.pop()
        elif i == 'D':
            stack.append(stack[-1] * 2)
        else:
            stack.append(int(i))
    return sum(stack)


print(sol(["5", "2", "C", "D", "+"]))
print(sol(["5", "-2", "4", "C", "D", "9", "+", "+"]))
