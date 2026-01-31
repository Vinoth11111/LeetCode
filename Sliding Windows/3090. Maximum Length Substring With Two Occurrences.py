# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/description/?envType=problem-list-v2&envId=sliding-window
def sol(s):
    res = 0
    has = {}
    left = 0
    for i in range(len(s)):
        has[s[i]] = has.get(s[i], 0) + 1

        while has[s[i]] > 2:
            has[s[left]] -= 1
            left += 1

        res = max(res, i-left+1)
    return res


print(sol("bcbbbcba"))
print(sol('aaaa'))
