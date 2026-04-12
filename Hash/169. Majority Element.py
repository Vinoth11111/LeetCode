def sol(nums):
    has = {}
    n = len(nums)
    if n == 1:
        return nums[0]
    for i in nums:
        if i not in has:
            has[i] = 1
        elif has[i] >= n//2:
            return i
        else:
            has[i] += 1


print(sol([2,2,1,1,1,2,2]))
print(sol([3,2,3]))