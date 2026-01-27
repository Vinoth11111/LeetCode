#https://leetcode.com/problems/contains-duplicate-ii/?envType=problem-list-v2&envId=array

def check(nums,k):
    memory = dict()
    i = 0
    while i < len(nums):
        num = nums[i]
        if memory.get(num) is not None and abs(memory[num]-i) <= k:
            return True

        memory[num] = i
        i += 1
    return False


print(check(nums=[1, 2, 3, 1, 2, 3], k=2))
print(check([1, 2, 3, 1], 3))
