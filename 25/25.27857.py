import math

max_count = 0
min_number = 0

for i in range(84052, 84131):
    count = 0
    stop = round(math.sqrt(i))
    for delitel in range(1, stop):
        if i % delitel == 0 and delitel != (i // delitel):
            count += 2
        elif i % delitel == 0 and delitel == (i // delitel):
            count += 1
    if count > max_count:
        max_count = count
        min_number = i

print(max_count, min_number)
