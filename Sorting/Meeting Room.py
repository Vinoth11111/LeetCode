# we were given a list of tuples and if we hav overlaping time return false return True
# https://blog.unwiredlearning.com/meeting-rooms
def sol(intervals):
    if not intervals:
        return True
    intervals.sort()
    for i in range(1,len(intervals)):
        if intervals[i-1][1] > intervals[1][0]:
            return False
    return True


print(sol([[1, 3], [4, 6], [5, 7], [8, 10]]))  # false
print(sol([[5, 5], [10, 10]]))  # True
print(sol([[5, 5], [5, 10]]))  # True
print(sol([[0, 1000000], [1000000, 2000000]]))  # true
print(sol([[0, 1000000], [999999, 2000000]]))  # false
print(sol([[1, 4], [2, 5], [3, 6]]))  # false
print(sol([[0, 30], [5, 10], [15, 20]]))  # false
print(sol([]))
