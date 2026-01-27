# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/submissions/1812170580/?envType=study-plan-v2&envId=leetcode-75

def check(s, k):
    counts = 0
    vow = ['a', 'e', 'i', 'o', 'u']
    for i in range(k):
        if s[i] in vow:
            counts += 1
    max_count = counts
    for i in range(k, len(s)):
        if k == max_count:
            return max_count
        if s[i-k] in vow:
            counts -= 1
        if s[i] in vow:
            counts += 1
        max_count = max(max_count, counts)
    return max_count


print(check("leetcode", 3))
print(check("aeiou", 2))
print(check('lettac', 3))