# https://leetcode.com/problems/defanging-an-ip-address/description/?envType=problem-list-v2&envId=string
def sol(add):
    res = ''
    for i in add:
        if i == '.':
            res += '[.]'
        else:
            res += i
    return res


print(sol("1.1.1.1"))
