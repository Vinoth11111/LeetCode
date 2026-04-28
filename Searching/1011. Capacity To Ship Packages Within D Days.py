# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

def sol(weights, days):
    left = max(weights)
    right = sum(weights)
    while left < right:
        mid = (left + right)//2
        required_days = 1
        current_capacity = 0
        for weight in weights:
            if current_capacity + weight > mid:
                current_capacity = 0
                required_days += 1
            current_capacity += weight
        if required_days > days:
            left = mid + 1
        else:
            right = mid
    return left

    


print(sol(weights=[1,2,3,4,5,6,7,8,9,10], days=5)) # 15
print(sol(weights=[1,2,3,1,1], days=4)) # 6
