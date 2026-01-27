# https://leetcode.com/problems/counting-bits/
def countBits(n: int):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp


print(countBits(3))
print(countBits(4))