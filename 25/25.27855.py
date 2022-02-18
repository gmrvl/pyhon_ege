import math

for i in range(95632, 95701):
    stop = int(math.sqrt(i))
    deliteli = []
    for d in range(1, stop):
        if i % d == 0:
            if d % 2 == 0:
                deliteli.append(d)
            if (i // d) % 2 == 0:
                deliteli.append(i // d)

    if len(deliteli) == 6:
        print(deliteli, i)
