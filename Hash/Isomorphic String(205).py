# https://leetcode.com/problems/isomorphic-strings/description/
def sol(s, t):
    if len(set(s)) != len(set(t)):
        return False
    s_has = {}
    for ss, tt in zip(s, t):
        if ss not in s_has:
            s_has[ss] = tt

    for i, val in enumerate(s):
        if s_has[val] != t[i]:
            return False
    return True


print(sol("egg", "add"))
print(sol("foo", "bar"))
print(sol("paper", "title"))
print(sol("bbbaaaba", "aaabbbba"))
