import math

for i in range(95632, 95651):
    stop = int(math.sqrt(i))
    a = []
    for j in range(1, stop):
        if i % j == 0:
            if j % 2 != 0:
                a.append(j)
            if i // j % 2 != 0:
                a.append(i // j)
            if len(a) > 6:
                break
    if len(a) == 6:
        print(sorted(a))
