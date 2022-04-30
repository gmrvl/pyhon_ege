file = open('33771.txt')

first = file.readline().split()

s = int(first[1])
a = []
for i in range(0, 1000):
    a.append(0)
count = 0
for d in file:
    p, c, t = d.split()
    p = int(p)
    c = int(c)
    if t == 'B':
        s -= p*c
    else:
        a[p] += c

for i in range(0, len(a)):
    if s - (i * a[i]) >= 0:
        s -= i * a[i]
        count += a[i]
    else:
        if s - i < 0:
            break
        else:
            while s - i >= 0:
                count += 1
                s -= i
print(s, count)
