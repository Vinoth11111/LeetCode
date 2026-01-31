# https://leetcode.com/problems/range-sum-query-immutable/?envType=problem-list-v2&envId=array

class numarray:
    def __init__(self, nums):
        self.nums = nums

    def sumrange(self, left, right):
        res = 0
        for i in range(left, right+1):
            res += self.nums[i]
        return res


nums = [-2, 0, 3, -5, 2, -1]
arr = numarray(nums)
val = [[arr.__init__(nums)], [arr.sumrange(0, 2)], [arr.sumrange(2, 5)], [arr.sumrange(0, 5)]]
print(val)
