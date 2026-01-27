# https://leetcode.com/problems/count-number-of-nice-subarrays/
def sol(array, max_odd):
    def at_most(nums, k):
        res = 0
        odd_count = 0
        left = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                odd_count += 1
            while odd_count > k:
                if nums[left] % 2 == 1:
                    odd_count -= 1
                left += 1
            res += i-left+1

        return res
    return at_most(array, max_odd) - at_most(array, max_odd-1)


print(sol([1, 1, 2, 1, 1], 3))
print(sol([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
