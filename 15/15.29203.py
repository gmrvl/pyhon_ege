# Для какого наименьшего целого неотрицательного числа А выражение
# (3x + 7y < A) ∨ (x ≥ y) ∨ (y > 6)
# тождественно истинно, т.е. принимает значение 1 при любых целых неотрицательных x и y?

def f(x, y, a):
    return (3*x + 7*y < a) or (x >= y) or (y > 6)

for a in range(1, 1000):
    ok = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if not f(x, y, a):
                ok = False
                break
    if ok:
        print(a)
        break