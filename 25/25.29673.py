import math

d = []
for i in range(123456789, 223456790):
    if (math.sqrt(i) % 1) == 0.0:
        d.append(i)

for i in d:
    a = []
    stop = int(math.sqrt(i))
    for dell in range(2, stop + 1):
        if i % dell == 0:
            a.append(dell)
            if dell != stop:
                a.append(i // dell)
    if len(a) == 3:
        a = sorted(a)
        print(i, a[2])



