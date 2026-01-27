#
def sol(s, k):
    has = {}
    max_rep = 0
    left = 0
    max_freq = 0
    for i in range(len(s)):
        has[s[i]] = has.get(s[i], 0) + 1
        max_freq = max(max_freq, has[s[i]])
        while (i - left + 1) - max_freq > k:
            has[s[left]] -= 1
            left += 1
        max_rep = max(max_rep, i - left + 1)
    return max_rep


print(sol("ABAB", 2))
print(sol("AABABBA", 1))
