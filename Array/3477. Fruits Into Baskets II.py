# https://leetcode.com/problems/fruits-into-baskets-ii/description/
def sol(fruits, baskets):
    temp = baskets[:]
    for i in fruits:
        for j in range(len(temp)):
            if i <= temp[j]:
                temp.pop(j)
                break
    return len(temp)


print(sol([4, 2, 5], [3, 5, 4]))
print(sol([3, 6, 1], [6, 4, 7]))
