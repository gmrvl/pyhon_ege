for i in range(38, 10000):
    x = i
    a = 3*x - 112
    b = 3*x + 58
    while a != b:
        print(a, b)
        if a > b:
            a -= b
        else:
            b -= a
    if a == 34:
        print(i)
        break
