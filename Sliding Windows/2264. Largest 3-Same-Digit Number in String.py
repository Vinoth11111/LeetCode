# https://leetcode.com/problems/largest-3-same-digit-number-in-string/
def sol(num):
    max_digit = ''

    for i in range(len(num)-2):
        if num[i] == num[i+1] == num[i+2]:
            if not max_digit or num[i] > max_digit:
                max_digit = num[i]

    return max_digit * 3 if max_digit != '' else ''


print(sol("6777133339"))
print(sol("42352338"))
print(sol("2300019"))
