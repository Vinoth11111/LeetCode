def matrix_conversion(matrix):
    res = []
    for i in range(len(matrix)):
        res_ind = 0
        for num in matrix[i]:
            if i == 0:
                res.append([num])
            else:
                res[res_ind].append(num)
                res_ind += 1
    return res


print(matrix_conversion([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
