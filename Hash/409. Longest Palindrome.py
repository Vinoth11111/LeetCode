from collections import Counter
def sol(s):
    res = 0
    odd = False
    has = Counter(s)
    for i in has:
        if has[i] %2 ==0:
            res += has[i]
        else:
            res += has[i]-1
            odd = True


    return res+1 if odd else res
    

print(sol("abccccdd"))  # 7
print(sol("a"))  # 1
print(sol("bb"))  # 2
