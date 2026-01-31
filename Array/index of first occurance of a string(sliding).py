# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/?envType=problem-list-v2&envId=string
def strStr(haystack: str, needle: str) -> int:
    for i in range(len(haystack) - len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1


print(strStr(haystack="sadbutsad", needle="sad"))
# can also be solved by  find().
