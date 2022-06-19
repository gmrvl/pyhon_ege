# Для какого наибольшего целого неотрицательного числа A выражение
#
# (2x + 3y < 30) ∨ (x + y ≥ A)

def K(x, y, A):
    return (2*x + 3*y < 30) or (x + y >= A)

for A in range(0, 1000):
    ok = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if not K(x, y, A):
                ok = False
                break
    if ok:
        print(A)
