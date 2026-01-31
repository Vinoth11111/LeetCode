# https://leetcode.com/problems/find-words-containing-character/description/?envType=problem-list-v2&envId=string
def sol(words, x):
    res = []
    for i, val in enumerate(words):
        if x in val:
            res.append(i)
    return res


print(sol(["leet", "code"], 'e'))
print(sol(["abc", "bcd", "aaaa", "cbc"], 'a'))
