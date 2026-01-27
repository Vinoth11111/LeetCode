# https://leetcode.com/problems/find-pivot-index/?envType=problem-list-v2&envId=mlwk4i47
# optimal solution
"""def sol(nums):
    if not nums:
        return 0
    total_sum = sum(nums)
    left_sum = 0
    for i in range(len(nums)):
        right_sum = total_sum - nums[i] - left_sum
        if right_sum == left_sum:
            return i
        else:
            left_sum += nums[i]

    return -1"""


# my solution
def sol(nums):
    prefix_sum = [0]
    sufix_sum = [0]
    suf_ind = -1
    for i in range(len(nums)):
        if i == 0:
            continue
        else:
            prefix_sum.append(prefix_sum[i-1]+nums[i-1])
        if i == 0:
            continue
        else:
            sufix_sum.append(sufix_sum[i-1]+nums[suf_ind])
        suf_ind += -1

    count = 0
    for pre, suf in zip(prefix_sum, sufix_sum[::-1]):
        if pre == suf:
            return count
        count += 1
    return -1


print(sol([7, 3, 1, 3, 5, 6]))
print(sol([2, -1, 1]))
print(sol([1, 2, 3]))
