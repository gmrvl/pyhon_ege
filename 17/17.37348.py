file = open('37348.txt')

n2 = 0
n17 = 0
n2n17 = 0
count = 0
max_sum = 0

for d in file:
    d = int(d)

    if d % 34 == 0:
        continue
    elif d % 17 == 0:
        count += n2 + n2n17
        n2 += 1
    elif d % 2 == 0:
        count += n17 + n2n17
        n17 += 1
    else:
        count += (n2 + n17 + n2n17)
        n2n17 += 1

print(count)
