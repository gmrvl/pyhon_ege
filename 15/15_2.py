#  Укажите наименьшее целое значение А, при котором выражение
# (5k + 6n > 57) ∨ ((k ≤ A)  (n < A))
# истинно для любых целых положительных значений k и n.

def f(k, n, a):
    return (5 * k + 6 * n > 57) or (k <= a and n < a)


for a in range(1, 1000):
    ok = True
    for k in range(1, 1000):
        for n in range(1, 1000):
            if not f(k, n, a):
                ok = False
                break
    if ok:
        print(a)
        break
