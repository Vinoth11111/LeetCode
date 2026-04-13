"""
create a dictionary to store the indices of each number
iterate through the array and for each number when lenght >=3 find the last 3 indices
calculate the distance between the first and last index and multiply by 2 -> formula
=|a-b|+|b-c|+|c-a|
=|b-a|+|c-b|+|c-a|
=b-b+c+c-a-a
=2(c-a)

if current distance is smaller than the minimum distance we found so far we update the minimum distance
 
Time complexity is O(n) because we are iterating through the array once
Space complexity is O(n) because we are using a dictionary to store the indices of each number
"""


from collections import defaultdict
def sol(nums: list[int]) -> int:
    indices = defaultdict(list)
    min_dist = float('inf')
    for i, num in enumerate(nums):
        indices[num].append(i)
        if len(indices[num]) >= 3:
            a,b,c = indices[num][-3:]
            res = 2*(c-a)
            if res < min_dist:
                min_dist = res
    return min_dist if min_dist != float('inf') else -1


print(sol([1,2,3,4,5]))  # -1
print(sol([1,2,1,1,3])) # 6