# https://leetcode.com/problems/spiral-matrix/description/
def sol(matrix):
    pass


print(sol([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print(sol([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
"""
def lenLongestFibSubseq(arr):
    # Step 1: Create a set for quick lookup of elements
    indices = {num: i for i, num in enumerate(arr)}
    n = len(arr)
    
    # Step 2: Create a DP table
    dp = {}
    max_len = 0
    
    # Step 3: Check for all pairs of (i, j)
    for j in range(1, n):
        for i in range(j):
            # Check if arr[i] + arr[j] exists in the array before index i
            prev_num = arr[j] - arr[i]
            if prev_num in indices and indices[prev_num] < i:
                # The pair (arr[indices[prev_num]], arr[i], arr[j]) forms a Fibonacci subsequence
                dp[(i, j)] = dp.get((indices[prev_num], i), 2) + 1
                max_len = max(max_len, dp[(i, j)])

    return max_len if max_len >= 3 else 0

# Example Test Case
arr = [1, 2, 3, 4, 5, 6, 7, 8]
print("Length of Longest Fibonacci Subsequence:", lenLongestFibSubseq(arr))

"""