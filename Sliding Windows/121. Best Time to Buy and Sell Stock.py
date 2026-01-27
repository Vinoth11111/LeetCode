# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
def sol(prices):
    left = 0
    max_profit = 0
    for right in range(1, len(prices)):
        if prices[left] > prices[right]:
            left = right
        max_profit = max(max_profit, prices[right] - prices[left])
    return max_profit


print(sol([7, 1, 5, 3, 6, 4]))
print(sol([7, 6, 4, 3, 1]))
