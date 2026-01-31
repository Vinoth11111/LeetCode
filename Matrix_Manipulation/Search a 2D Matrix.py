# https://leetcode.com/problems/search-a-2d-matrix-ii/?envType=problem-list-v2&envId=array

# in this problem the given matrix is sorted in ascending order.
# so we have to start checking from top right to left.
# if the current element = target return true
# if cur element > target move left(col) to find the small element
# if the cur element is < target then move down(row) because big element may exist in row.
# if no element is found return False
# time complexity o(m+n) m is row and n is col
def sol(matrix,target):
    if not matrix or len(matrix) == 0:
        return False
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    return False


print(sol([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5))
print(sol([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],20))
print(sol([[-1,3]],3))

# my initial solution
# time complexity - o(m*n)- its not optimal


def sol1(matrix,target):
    for i in matrix:
        if target in i:
            return True
    return False


print(sol1([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5))
print(sol1([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],20))
print(sol1([[-1,3]],3))
