import math

for i in range(95632, 95650):
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    d5 = 0
    stop = round(math.sqrt(i))
    for dell in range(2, stop):
        if i % dell == 0:
            if dell % 2 == 1 and d1 == 0:
                d1 = dell
                if (i // dell) % 2 != 0 and (i // dell) != dell:
                    d2 = i // dell
            elif i % dell == 0 and d1 != 0 and d2 == 0:
                d2 = dell
                if (i // dell) % 2 != 0 and (i // dell) != dell:
                    d3 = i // dell
            elif i % dell == 0 and d1 != 0 and d2 != 0 and d3 == 0:
                d3 = dell
                if (i // dell) % 2 != 0 and (i // dell) != dell:
                    d4 = i // dell
            elif i % dell == 0 and d1 != 0 and d2 != 0 and d3 != 0 and d4 == 0:
                d4 = dell
                if (i // dell) % 2 != 0 and (i // dell) != dell:
                    d5 = i // dell
            elif i % dell == 0 and d1 != 0 and d2 != 0 and d3 != 0 and d4 != 0 and d5 == 0:
                d5 = dell
                if (i // dell) % 2 != 0 and (i // dell) != dell:
                    d1 = 0
                    break
    if d4 != 0 and d5 == 0 and i % 2 != 0:
        d5 = i

    if d1 != 0 and d5 != 0:
        print(1, d1, d2, d3, d4, d5)
