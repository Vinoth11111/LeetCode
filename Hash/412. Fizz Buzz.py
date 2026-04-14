"""
just a simple problem, but I want to practice the basic coding skills"""
def sol(n):
    res = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            res.append("FizzBuzz")
        elif i % 3 == 0:
            res.append("Fizz")
        elif i % 5 == 0:
            res.append("Buzz")
        else:
            res.append(str(i))
    return res


print(sol(3)) # ["1","2","Fizz"]
print(sol(5)) # ["1","2","Fizz","4","Buzz"]
