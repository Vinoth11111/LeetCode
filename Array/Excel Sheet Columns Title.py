# https://leetcode.com/problems/excel-sheet-column-title/?envType=problem-list-v2&envId=string

def convertToTitle(columnNumber: int) -> str:
    res = ""

    while columnNumber > 0:
        columnNumber -= 1
        res = chr((columnNumber % 26) + ord("A")) + res
        columnNumber //= 26

    return res


print(convertToTitle(26))
print(convertToTitle(6))
