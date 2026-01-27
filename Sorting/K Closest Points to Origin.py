# https://leetcode.com/problems/k-closest-points-to-origin/description/

def sol(points, k):
    def euclidean(point):
        return (((0-point[0])**2) + ((0-point[1])**2)) ** 0.5
    distance = []
    for i in points:
        distance.append((i, euclidean(i)))

    sort_val = sorted(distance, key=lambda x: x[1])
    return [i[0] for i in sort_val[:k]]


print(sol([[3, 3], [5, -1], [-2, 4]], 2))  # [[3,3],[-2,4]]
print(sol([[2, 2], [2, 2], [3, 3], [2, -2], [1, 1]], 4))  # [[1,1],[2,2],[2,2],[2,-2]]
