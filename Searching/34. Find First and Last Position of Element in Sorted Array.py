def sol(nums, target):
    if not nums or target not in nums:
        return [-1, -1]
    # first occurance of target.
    left = 0
    right = len(nums) - 1
    first = -1
    while left <= right:
        mid =(left + right) // 2
        if nums[mid] == target:
            first = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    # last occurance of target.
    left = 0
    right = len(nums) - 1
    last = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            last = mid
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return [first, last]


print(sol([5,7,7,8,8,10], 8)) # [3,4]
print(sol([5,7,7,8,8,10], 6)) # [-1,-1]
