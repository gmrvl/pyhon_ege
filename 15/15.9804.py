def f(x, a):
    return (x & 29 != 0) <= ((x & 17 == 0) <= (x & a != 0))


for a in range(1, 1000):
    ok = True
    for x in range(1, 1000):
        if not f(x, a):
            ok = False
    if ok:
        print(a)
        break




