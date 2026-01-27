# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

def sol(s):
    stack = []
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    return ''.join(stack)


print(sol("abbaca"))
print(sol("azxxzy"))
print(sol("aaaaaa"))
print(sol("aababaab"))
