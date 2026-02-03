# https://leetcode.com/problems/time-needed-to-buy-tickets/

def sol(tickets, k):
    time = 0
    for i in range(len(tickets)):
        if i <= k:
            time += min(tickets[i], tickets[k])
        else:
            time += min(tickets[i],tickets[k]-1)
    return time


print(sol([2,2,2], 2))  # Output: 6
print(sol([5,1,1,1], 0))  # Output:
