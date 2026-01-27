# https://leetcode.com/problems/binary-subarrays-with-sum/description/
def sol(nums, k):
    def at_most(num, k):
        if k < 0:
            return 0
        res = 0
        left = 0
        total_sum = 0
        for i in range(len(num)):
            total_sum += num[i]
            while total_sum > k:
                total_sum -= num[left]
                left += 1
            res += i - left + 1
        return res

    return at_most(nums, k) - at_most(nums, k - 1)


def sol1(nums, k):
    ans = 0
    cur_sum = 0
    has = {0: 1}
    for i in nums:
        cur_sum += i
        if cur_sum-k in has:
            ans += has[cur_sum-k]
        has[cur_sum] = has.get(cur_sum, 0)+1
    return ans


print(sol([1, 0, 1, 0, 1], 2))
print(sol([1, 1, 1, 1, 1, 1, 1], 4))

print(sol1([1, 0, 1, 0, 1], 2))
print(sol1([1, 1, 1, 1, 1, 1, 1], 4))
