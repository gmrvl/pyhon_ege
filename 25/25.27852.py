import math

for i in range(185311, 185331):
    a = []
    stop = int(math.sqrt(i))
    for j in range(1, stop):
        if i % j == 0:
            a.append(j)
            a.append(i // j)
        if len(a) > 4:
            break
    if len(a) == 4:
        print(sorted(a))