import math
otvet = [0, 0]
for i in range(326359, 421987):
    a = []
    stop = int(math.sqrt(i))
    for j in range(1, stop):
        if i % j == 0:
            a.append(j)
            a.append(i // j)
        if len(a) > 4:
            break
    if len(a) == 4:
        if a[3] - a[2] > otvet[1]-otvet[0]:
            otvet[0] = a[2]
            otvet[1] = a[3]
print(otvet)
