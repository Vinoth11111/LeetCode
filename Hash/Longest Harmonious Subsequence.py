# https://leetcode.com/problems/longest-harmonious-subsequence/description/?envType=problem-list-v2&envId=hash-table
def sol(nums):
    has = {}
    for i in nums:
        if i not in has:
            has[i] = 1
        else:
            has[i] += 1

    max_seq = 0
    for key in has:
        if key - 1 in has:
            max_seq = max(max_seq, has[key] + has[key - 1])
    return max_seq


print(sol([1, 3, 2, 2, 2, 3, 4]))
