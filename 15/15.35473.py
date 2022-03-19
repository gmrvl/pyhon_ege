# Для какого наименьшего натурального числа А формула
# ДЕЛ(A, 45) ∧ (ДЕЛ(750, x) → (¬ДЕЛ(A, x) → ¬ДЕЛ(120, x)))
# тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной x)?
def Del(x, y):
    return x % y == 0


def f(x, a):
    return (Del(a, 45)) and ((Del(750, x)) <= ((not Del(a, x)) <= (not Del(120, x))))


for a in range(1, 1000):
    ok = True
    for x in range(1, 1000):
        if not f(x, a):
            ok = False
            break
    if ok:
        print(a)
        break
