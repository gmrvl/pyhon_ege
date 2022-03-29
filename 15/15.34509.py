def f(x, A):
    return ((x & 28 != 0) or (x & 45 != 0)) <= ((x & 17 == 0) <= (x & A != 0))

# ctrl + alt + l

for A in range (0, 1000):
    ok = True
    for x in range(0, 1000):
        if not f(x, A):
            ok = False
            break
    if ok:
        print(A)
        break
