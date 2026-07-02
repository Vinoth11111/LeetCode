def sol(sequence, k):
    if not sequence or k <= 0 and k > len(sequence):
        return []
    x = []
    y = []
    temp = []

    for i in range(len(sequence)):
        if i > k-1 and i != len(sequence) - 1:
            temp.pop(0)
            temp.append(sequence[i])
            print(temp)
            x.append(temp[:])
        elif i == len(sequence) - 1:
            temp.pop(0)
            temp.append(sequence[i])
            y = temp
        else:
            temp.append(sequence[i])
            if i == k-1:
                x.append(temp[:])
                print('1',temp)
    return x, y


x, y = sol(sequence = [10, 20, 30, 40, 50, 60], k = 3)

print('x is ',x)
print('y is ',y)