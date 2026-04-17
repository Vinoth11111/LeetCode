def sol(letters,target):
    left = 0
    right = len(letters) - 1
    while left <= right:
        mid = (left + right) // 2
        if letters[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return letters[left % len(letters)]


print(sol(["c","f","j"], "a")) # "c"
print(sol(["c","f","j"], "c")) # "f"


def sol2(letters,target):
    ord_target = ord(target)
    for i in letters:
        if ord(i) > ord_target:
            return i
    return letters[0]


print(sol2(["c","f","j"], "a")) # "c"
print(sol2(["c","f","j"], "c")) # "f"
