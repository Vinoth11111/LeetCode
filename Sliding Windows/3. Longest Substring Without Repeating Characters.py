# https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
if we seen a duplicate character in between left: right, we can move the left pointer to the right until we remove the duplicate character,
we can keep track of the max length of the substring without repeating characters.
time complexity: O(n)
space complexity: O(1)
"""
def sol(s):
    left = 0
    max_len = 0

    for i in range(len(s)):
        while s[i] in s[left:i]:
            left += 1
        max_len = max(max_len, i - left + 1)
    return max_len


print(sol("abcabcbb"))  # 3
print(sol("bbbbb"))  # 1
