import math

for i in range(312614, 312652):
    dell = []
    stop = int(math.sqrt(i))

    for d in range(1, stop):
        if i % d == 0:
            dell.append(d)
            dell.append(i // d)
            if len(dell) > 6:
                break
    if len(dell) == 6:
        print(sorted(dell))
