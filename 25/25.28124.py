import math

max_count = 0
c = 0
for i in range(568023, 569231):
    count = 0
    stop = int(math.sqrt(i))
    for dell in range(1, stop):
        if i % dell == 0:
            if i % dell == dell:
                count += 1
            else:
                count += 2
    if count > max_count:
        max_count = count
        c = i
print(max_count, c)
