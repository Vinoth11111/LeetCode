# https://leetcode.com/problems/first-unique-character-in-a-string/description/
def sol(s):
    has = {}
    for i in s:
        has[i] = has.get(i, 0) + 1
    for i in has:
        if has[i] == 1:
            return s.index(i)
    return -1


print(sol('leetcode'))
print(sol('loveleetcode'))
print(sol('aabb'))
print(sol('a'*100+'c'))
