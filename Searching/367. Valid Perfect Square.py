"""
in this problem we take the number and seperate it into linear space
we find the mid in the linear space and check if the mid*mid is equal to the number or not
if squared number is greater we have to move toward left(we want smaller number)
if squared number is smaller we move right(we want bigger number)
if left and right met then we have no perfect square and we return false
Time complexity is O(log(n)) because we are using binary search
Space complexity is O(1) because we are using constant space
"""


def sol(num: int) -> bool:
    l = 1
    r = num
    while l <= r:
        mid = (l+r)//2
        squared = mid*mid
        if squared == num:
            return True
        elif squared > num:
            r = mid -1
        elif squared < num:
            l = mid + 1
    return False


print(sol(16))  # True
print(sol(14))  # False