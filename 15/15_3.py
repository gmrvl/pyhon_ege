#  Для какого наибольшего целого неотрицательного числа A выражение
# (y + 2x ≠ 48) ∨ (A < x) ∨ (x < y)
# тождественно истинно, то есть принимает значение 1 при любых целых неотрицательных x и y?

def f(x, y, a):
    return (y + 2*x != 48) or (a < x) or (x < y)


for a in range(1, 1000):
    ok = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not f(x, y, a):
                ok = False
                break
    if ok:
        print(a)