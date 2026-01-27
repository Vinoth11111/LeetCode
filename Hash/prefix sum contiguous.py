# https://leetcode.com/problems/subarray-sum-equals-k/

def subarraysum(nums, k) -> int:
    counts = 0
    has = {0: 1}
    sum_val = 0
    for cur in nums:
        sum_val += cur
        if sum_val - k in has:
            counts += has[sum_val-k]
        if sum_val not in has:
            has[sum_val] = 1
        else:
            has[sum_val] += 1
        print(has)

    return counts


print(subarraysum([1, -1, 0], 0))
