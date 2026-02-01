# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/?envType=problem-list-v2&envId=hash-table

from collections import Counter

from attr import has

def sol(s):
    has = Counter(s)
    vow = ['a','e','i','o','u']
    con_sum = 0
    vow_sum = 0
    for i in has:
        if i in vow:
            vow_sum = has[i] if has[i] > vow_sum else vow_sum
        else:
            con_sum = has[i] if has[i] > con_sum else con_sum 
    return vow_sum + con_sum


print(sol("successes")) 
