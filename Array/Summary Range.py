#https://leetcode.com/problems/summary-ranges/description/?envType=problem-list-v2&envId=mlwk4i47

def sol(nums):
    res = []
    start = nums[0]

    for i in range(1,len(nums)):
        if nums[i] != nums[i-1] +1:
            if start == nums[i-1]:
                res.append(start)

            else:
                res.append(f'{start}->{nums[i-1]}')
            start = nums[i]
    if start == nums[-1]:
        res.append(start)
    else:
        res.append(f'{start}->{nums[-1]}')
    return res


print(sol([0, 1, 2, 4, 5, 7]))
print(sol([0, 2, 3, 4, 6, 8, 9]))
