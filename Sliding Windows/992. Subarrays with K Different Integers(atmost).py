# https://leetcode.com/problems/subarrays-with-k-different-integers/
# if we don't use the 2 user define function and want to solve in 1
# we have to use 2 pointer approach where we have 2 left1 and left2 we have to use 2 while loop to calculate the len of substring.
# similar problem.
# 1️⃣ 1248. Count Number of Nice Subarrays
# 2️⃣ 930. Binary Subarrays With Sum
# 4️⃣ 1358. Number of Substrings Containing All Three Characters
# 5️⃣ 2024. Maximize the Confusion of an Exam
# 6️⃣ 1004. Max Consecutive Ones III

def sol(nums, k):

    def at_most(nums, k):
        res = 0
        has = {}
        left = 0
        for i in range(len(nums)):
            has[nums[i]] = has.get(nums[i], 0) +1
            while len(has) > k:
                has[nums[left]] -= 1
                if has[nums[left]] == 0:
                    del has[nums[left]]
                left += 1
            res += i-left+1
        return res
    return at_most(nums, k) - at_most(nums, k-1)


print(sol([1, 2, 1, 2, 3], 2))
print(sol([1, 2, 1, 3, 4], 3))

