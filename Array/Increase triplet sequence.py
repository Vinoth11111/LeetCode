def rip(nums):
    first = float('inf')
    second = float('inf')
    for i in nums:
        if i <= first:
            first = i
        elif i <= second:
            second = i
        else:
            return True

    return False


print(rip([5,4,3,2,1]))

#https://leetcode.com/problems/increasing-triplet-subsequence/?envType=study-plan-v2&envId=leetcode-75
