# https://leetcode.com/problems/task-scheduler/description/
from collections import Counter


# we have to find the max freq in the task so we can create the interval, then for creating the interval we have the value n. we have place values only after the interval which mean n + 1
# we use max_freq-1 because last block does not neet cooldown.
# In some case we have more than 2 max_freq so we have to take accountable for that.
# if we have n = 0 then whole term will be zero so we have to return the length of the interval in this case.
def sol(tasks, n):
    has = Counter(tasks)
    max_freq = max(has.values())
    max_count = sum([1 for i in has.values() if i == max_freq])

    interval = (max_freq - 1) * (n+1) + max_count
    return max(len(tasks), interval)

# formula -> interval = max_freq -1 * n-1 + no_of_max_freq_count


print(sol(["A", "A", "A", "B", "B", "B"], 2))
print(sol(["A", "C", "A", "B", "D", "B"], 1))
print(sol(["A", "A", "A", "B", "B", "B"], 3))
