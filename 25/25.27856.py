import math

for i in range(95632, 95651):
    dell = []
    stop = int(math.sqrt(i))
    for d in range(1, stop):
        if i % d == 0:
            if d % 2 == 1:
                dell.append(d)
            if (i // d) % 2 == 1:
                dell.append(i // d)
            if len(dell) > 6:
                break
    if len(dell) == 6:
        print(sorted(dell))