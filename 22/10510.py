for i in range(40, 1000):
    x = i
    L = x
    M = 12
    if L % 2 == 0:
        M = 24
    while L != M:
        if L > M:
            L -= M
        else:
            M -= L
    if M ==2:
        print(i, M)
        break