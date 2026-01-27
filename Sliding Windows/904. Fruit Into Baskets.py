# https://leetcode.com/problems/fruit-into-baskets/

def sol(fruits):
    bucket = {}
    max_fruits = 0
    left = 0
    for i in range(len(fruits)):
        bucket[fruits[i]] = bucket.get(fruits[i],  0) + 1

        while len(bucket) > 2:
            bucket[fruits[left]] -= 1
            if bucket[fruits[left]] == 0:
                del bucket[fruits[left]]
            left += 1
        max_fruits = max(max_fruits,  i - left + 1)
    return max_fruits


print(sol([1, 2, 1]))
print(sol([0, 1, 2, 2]))
print(sol([1, 2, 3, 2, 2]))
print(sol([1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]))
