# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/?envType=problem-list-v2&envId=string
def finalValueAfterOperations(operations):
    if not operations:
        return 0
    res = 0
    for i in operations:
        if i == '++X' or i == 'X++':
            res += 1
        else:
            res -= 1
    return res


print(finalValueAfterOperations(["--X", "X++", "X++"]))
print(finalValueAfterOperations(["++X", "++X", "X++"]))
