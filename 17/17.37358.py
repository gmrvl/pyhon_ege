file = open('37358.txt')

count = 0
max_pair = 0

a = []
max_m = []
max0 = 0
max5 = 0
for i in range(10):
    a.append(0)
    max_m.append(0)

for i in file:
    i = int(i)
    if i % 10 == 0:
        count += a[0]
        if i > max_m[0]:
            max_m[0] = i
        elif i > max0:
            max0 = i
    elif i % 10 == 5:
        count += a[5]
        if i > max_m[5]:
            max_m[5] = i
        elif i > max5:
            max5 = i
    else:
        count += a[10 - (i % 10)]
        if i > max_m[i % 10]:
            max_m[i % 10] = i
    a[i % 10] += 1

if max0 + max_m[0] > max5 + max_m[5]:
    max_pair = max0 + max_m[0]
else:
    max_pair = max5 + max_m[5]
for i in range(1, 5):
    if max_m[i] + max_m[10-i] > max_pair:
        max_pair = max_m[i] + max_m[10-i]
print(count, max_pair)
