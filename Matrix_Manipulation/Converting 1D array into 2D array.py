# https://leetcode.com/problems/convert-1d-array-into-2d-array/
# my solution
def sol(nums, m, n):
    res = []
    if len(nums) != (m*n):
        return []
    col = n
    row = 0
    for num in nums:
        if col == n:
            res.append([num])
            col -= 1
        elif col != 0:
            res[row].append(num)
            col -= 1
        if col == 0:
            row += 1
            col = n
    return res


print(sol([1, 2, 3, 4], 2, 2))
print(sol([1, 3, 3, 5], 3, 1))


# optimal solution
def solu(nums, m, n):
    if len(nums) != m*n:
        return []
    res = []
    for i in range(m):  # creating the m number of rows
        # slicing num into corresponding rows
        res.append(nums[i*m:(i+1)*m])
    return res


print(solu([1, 2, 3, 4], 2, 2))
print(solu([1, 3, 3, 5], 3, 1))
