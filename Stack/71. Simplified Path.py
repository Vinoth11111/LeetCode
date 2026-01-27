# https://leetcode.com/problems/simplify-path/description/

def sol(paths):
    path = paths.split('/')
    stack = []
    for i in path:
        if i == '':
            continue
        elif i == '..' or i == '.':
            if stack:
                stack.pop()
        else:
            stack.append(i)
    if not stack:
        return '/'
    else:
        return '/' + '/'.join(stack)


print(sol("/home/"))
print(sol("/home//foo/"))
print(sol("/home/user/Documents/../Pictures"))