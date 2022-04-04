def F(x, y, A):
    return (5*x - 6*y < A) or (x - y > 30)

for A in range(0, 1000):
    ok = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if not F(x, y, A):
                ok = False
                break
    if ok:
        print(A)
        break