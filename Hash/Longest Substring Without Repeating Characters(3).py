# https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=problem-list-v2&envId=hash-table

def sol(s) -> int:
    res = 0
    seen = []
    for i in s:
        if i not in seen:
            seen.append(i)
            res = max(res, len(seen))
        else:
            while i in seen:
                seen.pop(0)
            seen.append(i)
            res = max(res, len(seen))

    return res


def sol1(s):
    res = 0
    seen = set()
    left = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        res = max(res, right - left + 1)
    return res


print(sol("abcabcbb"))
print(sol("bbbbb"))
print(sol("pwwkew"))
print(sol("dvdf"))
print(sol("ckilbkd"))
