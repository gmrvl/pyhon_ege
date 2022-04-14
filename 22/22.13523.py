m = 0
while True:
    x = m
    S = x
    R = 0
    while x > 0:
        d = x % 2
        R = 10 * R + d
        x = x // 2
    S = R + S
    if 9999 < S < 100000:
        print(m)
        break

    m += 1