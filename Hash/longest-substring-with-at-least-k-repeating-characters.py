a = [[1,2,3],[4,5,6],[7,8,9]]
res =[]
for i in range(len(a)):
    res_ind = 0
    for num in a[i]:
        if i == 0:
            res.append([num])
        else:
            res[res_ind].append(num)
            res_ind+=1


print(res)