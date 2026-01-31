# https://leetcode.com/problems/crawler-log-folder/description/

def sol(logs):
    res = 0
    for i in logs:
        if i != '../' and i != './':
            res += 1
        elif i == '../' and res != 0:
            res -= 1
    return res


print(sol(["d1/", "d2/", "../", "d21/", "./"]))
print(sol(["d1/", "d2/", "./", "d3/", "../", "d31/"]))
