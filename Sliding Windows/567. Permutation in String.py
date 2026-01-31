# https://leetcode.com/problems/permutation-in-string/
from collections import Counter


def sol(s1, s2):
    if len(s1) > len(s2):
        return False
    s1_has = Counter(s1)
    s2_has = {}
    left = 0
    for i in range(len(s2)):
        s2_has[s2[i]] = s2_has.get(s2[i], 0) + 1
        while i-left+1 > len(s1):  # here we compare the length of original string with the windowed string.
            s2_has[s2[left]] -= 1
            if s2_has[s2[left]] == 0:
                del s2_has[s2[left]]
            left += 1
        if s1_has == s2_has:
            return True
    return False


print(sol("ab", "eidbaooo"))
print(sol("ab", "eidboaoo"))
