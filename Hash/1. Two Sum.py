# https://leetcode.com/problems/two-sum/description/
"""
create has map to store the value and index of the number in the array
for each element find target - current element exist in tha has map
if exist return the index of the current element and the index of the required element
if not add the current element and its index to the has map
"""
def sol(nums, traget):
    has = {}
    for i in range(len(nums)):
        required = traget - nums[i]
        if required in has:
            return [has[required], i]
        has[nums[i]] = i
    return []


print(sol([2,7,11,15], 9)) # [0,1]
print(sol([3,2,4], 6)) # [1,2]
