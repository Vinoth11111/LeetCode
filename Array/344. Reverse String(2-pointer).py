# https://leetcode.com/problems/reverse-string/description/

def sol(s):
    left = 0
    right = len(s)-1

    while left < right:
        s[left],s[right] = s[right],s[left]
        left += 1
        right -= 1
    return s


print(sol(["h","e","l","l","o"])) # ["o","l","l","e","h"]
print(sol(["H","a","n","n","a","h"])) # ["h","a","n","n","a","H"]
