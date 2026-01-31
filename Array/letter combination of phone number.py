# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

def phone_str(digits):
    if digits == '1':
        return ''

    key_map = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
    permutation = []
    n = len(digits)
    if n == 1:
        permutation.extend(key_map.get(digits))
        return permutation

print(phone_str('2'))