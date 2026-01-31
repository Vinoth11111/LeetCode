# https://leetcode.com/problems/uncommon-words-from-two-sentences/?envType=problem-list-v2&envId=hash-table
def sol(s1, s2):
    has = {}
    for i in s1.split():
        has[i] = has.get(i, 0) + 1

    for i in s2.split():
        has[i] = has.get(i, 0) + 1

    res = []

    for i in has:
        if has[i] == 1:
            res.append(i)
    return res


print(sol("this apple is sweet", "this apple is sour"))
print(sol("apple apple", "banana"))
print(sol("abcd def abcd xyz", "ijk def ijk"))
print(sol("s z z z s", "s z ejt"))
