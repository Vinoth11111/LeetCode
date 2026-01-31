# https://leetcode.com/problems/find-the-duplicate-number/description/
def sol(nums: list[int]) -> int:
    # floyd-tortoise-hare problem
    # 2 pointer approach, slow(tortoise) and fast(hare)
    # since the duplicated is guarantee at some point they met each other because of cycle(cycle-detection)
    # we have reset to  fast ind to zero for duplicate detection.
    # if fast != slow return slow (duplicate)
    # time and space complexity o(n) and 0(1)
    slow = nums[0]
    fast = nums[nums[0]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    # if we detect a cycle
    fast = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow


print(sol([1, 3, 4, 2, 2]))
print(sol([3, 3, 3, 3, 3]))
