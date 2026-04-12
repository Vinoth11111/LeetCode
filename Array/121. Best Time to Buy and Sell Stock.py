# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
"""
find the minimum price so far
if the current price is less than the minimum price we update the minimum price
if the current profit is greater than the maximum profit we update the maximum profit
Time complexity is O(n) because we are iterating through the array once
Space complexity is O(1) because we are using constant space
"""
def sol(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit


print(sol([7, 1, 5, 3, 6, 4]))  # 5
print(sol([7, 6, 4, 3, 1]))  # 0