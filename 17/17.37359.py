file = open('37359.txt')

a = []
max_d = []
max_0 = 0
count = 0
max_pair = 0


for i in range(117):
    a.append(0)
    max_d.append(-10000)

for d in file:
    d = int(d)
    ost = d % 117
    if ost == 0:
        count += a[ost]
        if max_0 < d <= max_d[0]:
            max_0 = d
    else:
        count += a[117 - ost]
    a[ost] += 1

    if d > max_d[ost]:
        max_d[ost] = d

max_pair_massive = []

max_pair_massive.append(max_d[0] + max_0)

for i in range(1, int(117/2)):
    max_pair_massive.append(max_d[i]+max_d[117-i])

max_pair = max(max_pair_massive)
print(max_pair)
