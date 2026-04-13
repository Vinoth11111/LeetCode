"""
if a value appears more than twice, return false
if not return true
"""
def sol(nums):
    has= {}
    for num in nums:
        if num not in has:
            has[num] = 1
        else:
            has[num] += 1
            if has[num] > 2:
                return False
    return True


print(sol([1,1,2,2,3,4])) # True
print(sol([10,10])) # True
print(sol([1,1,1,1])) # False