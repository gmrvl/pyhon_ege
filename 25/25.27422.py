import math

for i in range(174457, 174506):
    deliteli = []
    stop = int(math.sqrt(i))
    for d in range(1, stop):
        if i % d == 0:
            deliteli.append(d)
            deliteli.append(i // d)
    if len(deliteli) == 4:
        print(deliteli)
