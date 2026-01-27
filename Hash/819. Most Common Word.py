# https://leetcode.com/problems/most-common-word/?envType=problem-list-v2&envId=hash-table
import re


def sol(paragraph, banned):
    word = re.findall(r'[A-Za-z]+', paragraph)
    has = {}
    for i in word:
        w = i.lower()
        if w not in banned:
            has[w] = has.get(w, 0) + 1

    res = ''
    freq = 0
    for i in has:
        if has[i] > freq:
            res = i
            freq = has[i]
    return res


print(sol("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
print(sol("a, a, a, a, b,b,b,c, c", ['a']))
