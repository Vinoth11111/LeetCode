# https://leetcode.com/problems/decode-string/
def sol(s):
    stack = []
    for i in s:
        if i == ']':
            vals = ''
            while stack[-1] != '[':
                vals = stack.pop() + vals
            stack.pop()  # remove the '[' opening bracket
            num = ''  # if we have more than a single digit
            while stack and stack[-1].isdigit():
                num = stack.pop() + num

            stack.append(int(num) * vals)  # adding the decoded sequence to the stack
        else:
            stack.append(i)
    return ''.join(stack)


print(sol("3[a]2[bc]"))
print(sol("3[a2[c]]"))
print(sol("2[abc]3[cd]ef"))
print(sol("11[2[a]]"))
