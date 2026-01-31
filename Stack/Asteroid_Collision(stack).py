# https://leetcode.com/problems/asteroid-collision/?envType=study-plan-v2&envId=leetcode-75

def sol(astroids):
    res = []
    for i in astroids:
        temp = i
        while (temp < 0) and (len(res)) > 0:
            if (res[-1] > 0) and (abs(temp) > res[-1]):  # if previous astroids is pos and small remove previous astroids
                res.pop()
            elif abs(temp) < res[-1]:  # if curr astroids is small we remove
                temp = 0
            elif abs(temp) == res[-1]:  # if both astroids is same size we remove both
                res.pop()
                temp = 0
            else:
                break
        if temp:
            res.append(temp)
    return res


print(sol([5, 10, -5]))
print(sol([3, 5, -6, 2, -1, 4]))
print(sol([-2, -1, 1, 2]))
print(sol([10, 2, -5]))
print(sol([8, -8]))
