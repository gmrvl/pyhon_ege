for i in range(150_000_000, 300_000_001):
    x = i
    m = 0
    n = 0
    while x % 2 == 0:
        x /= 2
        m += 1
    if m % 2 == 0:
        while x % 3 == 0:
            x /= 3
            n += 1
        if x == 1 and n % 2 == 1:
            print(i, m + n)
    else:
        continue

