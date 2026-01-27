"""Similar Problems You Can Solve Using This Pattern:
Subarray Sum Equals K:
Given an array of integers, find the length of the longest subarray whose sum equals a given target k.

Transformation: Track the running sum of the array, and store the first occurrence of each running sum in a hash map. If current_sum - k has been seen before, you have found a subarray that sums to k.
Subarray with Equal Number of 0's and 1's in an Unsorted Array:
You can apply the same logic when the array is unsorted, and you're looking for subarrays that balance two elements (like 0 and 1), treating one of them as -1.

Longest Substring with At Most K Distinct Characters:
In problems related to substrings with a certain number of distinct elements, you can track the frequency of characters using a sliding window technique and hash map to get the result efficiently.

Find the Longest Subarray with Equal Even and Odd Numbers:
Treat even numbers as +1 and odd numbers as -1, and then use the same approach to find subarrays where the count of even and odd numbers are equal.

Longest Subarray with K Distinct Elements:
Here, you could use a sliding window approach along with a hash map to keep track of the count of distinct elements within the window. When the number of distinct elements exceeds k, you shrink the window from the left side until you are back to k distinct elements."""

def sol(nums):
    mos_con = 0
    vals = 0
    has = {
        0: -1
    }

    for i in range(len(nums)):
        if nums[i] == 0:
            val = -1
        else:
            val = 1
        vals += val
        if vals not in has:
            has[vals] = i
        else:
            mos_con = max(mos_con,i - has[vals])
    return mos_con

print(sol([0,1]))
print(sol([0,1,1,1,1,1,0,0,0]))
print(sol([0,1,0]))