# https://leetcode.com/problems/group-anagrams/description/?envType=problem-list-v2&envId=hash-table
def sol(nums: list) -> list:
    has = {}
    for char in nums:
        sor = ''.join(sorted(char))
        if sor not in has:
            has[sor] = [char]
        else:
            has[sor].append(char)
    return list(has.values())


print(sol(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(sol(['']))
print(sol(['a']))
