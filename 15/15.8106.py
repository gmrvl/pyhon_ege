#  ¬ДЕЛ(x, А) → (ДЕЛ(x, 6) → ¬ДЕЛ(x, 4))

def Deel(x, A):
    return x % A == 0


def K(x, A):
    return (not Deel(x, A)) <= ((Deel(x, 6)) <= (not Deel(x, 4)))


for A in range(1, 1000):
    ok = True
    for x in range(1, 1000):
        if not K(x, A):
            ok = False
            break
    if ok:
        print(A)
