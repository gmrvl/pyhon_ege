
# наибольшее, сначала 3, а потом 8.

for i in range (0, 1000):
    x = i
    L = 0
    M = 0

    while x > 0:
        L = L + 1
        if x % 2 == 0:
            M = M + (x % 10)
        x = x // 10
    if L==3 and M==8:
        print(i, L, M)
