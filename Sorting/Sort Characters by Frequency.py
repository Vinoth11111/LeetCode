# https://leetcode.com/problems/sort-characters-by-frequency/description/
from collections import Counter


def sol(s) -> str:
    frequency = []
    res = ''
    for i in set(s):
        frequency.append((i, s.count(i)))
    frequency.sort(key=lambda x: x[1], reverse=True)  # we can also use counter with ranking: -has[x] (-) means sort by highest value to lowest.

    for i in frequency:
        res += i[0] * i[1]

    return res


def sol1(s):
    has = Counter(s)
    chars = list(s)
    chars.sort(key=lambda x: (-has[x], x))  # -[has[x]] means sort by descending order
    return ''.join(chars)


print(sol("tree"))
print(sol("loveleetcode"))
print(sol("cccaaa"))
print(sol("Aabb"))
print(sol1("tree"))
print(sol1("loveleetcode"))
print(sol1("cccaaa"))
print(sol1("Aabb"))
