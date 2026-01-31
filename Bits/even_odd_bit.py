# https://leetcode.com/problems/number-of-even-and-odd-bits/

def evenOddBit(n):
    # Get the binary representation of n
    binary = bin(n)[2:]
    print(binary)
    num = binary[::-1]

    even = 0  # To count bits at even positions (1-based)
    odd = 0  # To count bits at odd positions (1-based)

    # Iterate through the binary representation
    for i in range(len(binary)):
        # Note: 1-based index is i + 1
        if i % 2 == 1:  # 1-based odd position
            odd += int(num[i])
        else:  # 1-based even position
            even += int(num[i])

    # Return the count of 1's at odd and even positions
    return [even, odd]


print(evenOddBit(50))
print(evenOddBit(5))
