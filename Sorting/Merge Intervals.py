# https://leetcode.com/problems/merge-intervals/description/

def sol(intervals):
    intervals.sort(key=lambda x: x[0])
    res = []
    for i in intervals:
        if not res or res[-1][1] < i[0]:
            res.append(i)
        else:
            res[-1][1] = max(i[1], res[-1][1])
    return res


print(sol([[4, 5], [2, 4], [4, 6], [3, 4], [0, 0], [1, 1], [3, 5], [2, 2]]))
print(sol([[1, 4], [0, 0]]))
