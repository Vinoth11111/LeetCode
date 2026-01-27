def check_seq(s, t):
    i = 0
    for char in t:
        if i < len(s) and s[i] == char:
            i += 1
    return i == len(s)


print(check_seq(s="abc", t="ahbgdc"))

# https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=leetcode-75
