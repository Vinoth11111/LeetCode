def zeros(nums):
    last_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_zero], nums[i] = nums[i], nums[last_zero]
            last_zero += 1
    return nums


a = [0, 0, 1]
print(zeros(a))
