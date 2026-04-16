# https://leetcode.com/problems/first-bad-version/
"""
find the first bad version using binary search.
we have two pointers left and right that point to the start and end of the versions.
we find the mid index and check if the mid version is bad or not using the isBad
if is bad find the first bad version in the left half of the versions by moving the right pointer to mid - 1.
if is not bad find the first bad version in the right half of the versions by moving the left pointer to mid + 1.
Time complexity is O(log(n)) because we are using binary search.
Space complexity is O(1) because we are using constant space.
"""
def isBadVersion(cur_version,bad):
    # This is a mock implementation of the isBadVersion API.
    # In a real scenario, this function would be provided by the system.
    return cur_version >= bad
def sol(ver,n):
    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
    
        if isBadVersion(bad=ver,cur_version=mid):
            right = mid - 1
        else:
            left = mid + 1
    return left # return first bad version


print(sol(ver=4,n=5)) # 4
print(sol(ver=7,n=10)) # 7
