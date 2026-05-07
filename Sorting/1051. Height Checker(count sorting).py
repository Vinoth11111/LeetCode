# https://leetcode.com/problems/height-checker/description/

def sol(heights):
    count = [0] * 101
    for h in heights:
        count[h] += 1

    res = 0
    cur_height = 0
    for h in heights:
        while count[cur_height] == 0:
            cur_height += 1

        if h != cur_height:
            res += 1
        count[cur_height] -= 1
    return res


print(sol([1,1,4,2,1,3])) # 3
print(sol([5,1,2,3,4])) # 5
