# https://leetcode.com/problems/find-all-duplicates-in-an-array/

def sol(nums):
    res = []  # duplicates
    for i in nums:
        # nums were presented as 1 -n so in-order to find the index we have to use i-1 eg: if when 1=8 we only have index 0-7
        ind = abs(i) - 1
        # if the curr index element is already seed(negative) then add the curr element to the duplicate
        if nums[ind] < 0:
            res.append(abs(i))  # may already been seen by other element so we have to abs
        else:
            nums[ind] = -nums[ind]
    return res


print(sol([4, 3, 2, 7, 8, 2, 3, 1]))
print(sol([1]))
print(sol([10, 2, 5, 10, 9, 1, 1, 4, 3, 7]))
print(sol([]))

"""

similar pattern.
you see these, think index-mapping immediately: -> when values are from 1-n,then:
Find All Duplicates in an Array
Find All Numbers Disappeared in an Array
First Missing Positive
Find the Duplicate Number
Set Mismatch
Missing Number

constraints:
space complexity 0(1)
"""