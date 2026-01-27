# https://leetcode.com/problems/jewels-and-stones/?envType=problem-list-v2&envId=string

def sol(jewels, stones):
    jewel = set(jewels)
    stone_cnt = 0
    for s in stones:
        if s in jewel:
            stone_cnt += 1
    return stone_cnt


print(sol("aA", '"aAAbbbb"'))
print(sol("z", "ZZ"))

# we can also solve this using hash map to reduce the lookup like AA as 2.
