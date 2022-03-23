def f(n):
    if n < 2:
        return 1
    else:
        if n % 3 == 0:
            return f(n/3) - 1
        else:
            return f(n - 1) + 7
for n in range(0, 100000):
    if f(n) == 111:
        print(n)
        break