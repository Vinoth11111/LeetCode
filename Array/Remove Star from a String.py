# https://leetcode.com/problems/removing-stars-from-a-string/?envType=study-plan-v2&envId=leetcode-75
def sol(s):
    word = []
    for i in s:
        if i != '*':
            word.append(i)
        else:
            word.pop()
    return ''.join(word)


print(sol("leet**cod*e"))
print(sol("erase*****"))
