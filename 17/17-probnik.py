file = open("17.37347.txt")

n2n7 = 0
n7d2 = 0
d7n2 = 0

max_n7n2 = 0
max_n7d2 = 0
max_d7n2 = 0
max_n7d2_2 = 0
max_d7n2_2 = 0
max_n7n2_2 = 0
maxx = 0

count = 0

for i in file:
    i = int(i)
    if i % 7 == 0 and i % 2 == 0:
        continue
    elif i % 7 != 0 and i % 2 != 0:
        count += n2n7
        count += n7d2
        count += d7n2
        n2n7 += 1
        if i > max_n7n2:
            max_n7n2_2 = max_n7n2
            max_n7n2 = i
        elif i > max_n7n2_2:
            max_n7n2_2 = i
    elif i % 7 != 0 and i % 2 == 0:
        count += n2n7
        count += n7d2
        n7d2 += 1
        if i > max_n7d2:
            max_n7d2 = i
        elif i > max_n7d2_2:
            max_n7d2_2 = i
    elif i % 7 == 0 and i % 2 != 0:
        count += n2n7
        count += d7n2
        d7n2 += 1
        if i > max_d7n2:
            max_d7n2 = i
        elif i > max_d7n2_2:
            max_d7n2_2 = i

maxx = max(max_n7n2+max_n7n2_2, max_d7n2+max_d7n2_2, max_n7n2 + max_n7d2, max_n7n2 + max_d7n2, max_d7n2 + max_d7n2_2)
print(count, maxx)
