for i in range(1, 100001):
    s = i
    n = 740
    while s + n < 1200:
        s = s + 6
        n = n - 4
    if n == 68:
        print(i)

