import math

for i in range(45000000, 50000001):
    a = []
    stop = int(math.sqrt(i))
    for j in range(1, stop):
        if i % j == 0:
            if j % 2 != 0:
                a.append(j)
            if i // j % 2 != 0:
                a.append(i // j)
            if len(a) > 5:
                break
    if len(a) == 5:
        print(sorted(a))
