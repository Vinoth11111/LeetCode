# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
def sol(heights):
    max_length = 0
    stack = []
    heights.append(0)  # for checking the boundary of last element with previous element

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]

            if not stack:
                width = i
            else:
                width = i - stack[-1] - 1  # right - left -1 1 is used for getting the boundaries excluding the values.
                # for example 5,6,5 when 5 boundary is 1 with out -1 it will be 2.
            max_length = max(max_length, height * width)
        stack.append(i)
    return max_length


print(sol([2, 1, 5, 6, 2, 3]))
print(sol([2, 4]))
