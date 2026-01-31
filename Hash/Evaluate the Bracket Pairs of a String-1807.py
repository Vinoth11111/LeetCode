# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/description/?envType=problem-list-v2&envId=hash-table
import re


def sol(s, knowledge):
    res = s
    has = dict(knowledge)
    word = re.findall(r'\(\w*\)', s)

    for i in word:
        res = re.sub(re.escape(i), has.get(i[1:-1], '?'), res)
    return res


def sol1(s, knowledge):
    has = dict(knowledge)
    s = s.replace(')', '(')
    word = s.split('(')
    for i in range(1, len(word), 2):
        if word[i] in has:
            word[i] = has[word[i]]
        else:
            word[i] = '?'

    return ''.join(word)


print(sol1("(name)is(age)yearsold", [["name", "bob"], ["age", "two"]]))
print(sol1("hi(name)", [["a", "b"]]))
print(sol("(name)is(age)yearsold", [["name", "bob"], ["age", "two"]]))
print(sol("hi(name)", [["a", "b"]]))
