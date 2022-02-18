file = open("33105.txt")

t_sum = 0
max_cost = 0
a = []

n = int(file.readline())

for i in file:
    d = int(i)
    if d <= 100:
        t_sum += d
    else:
        a.append(d)

a = sorted(a)

c = int(len(a)/2)
for i in range(0, len(a)):
    if i < c:
        t_sum += 0.7 * a[i]
    else:
        t_sum += a[i]

print(t_sum, a[c-1])




