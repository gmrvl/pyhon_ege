file = open('33105.txt')

a = []
first = int(file.readline())

sum_p = 0

for i in file:
    i = int(i)
    if i > 100:
        a.append(i)
    else:
        sum_p += i
a = sorted(a)
c = int(len(a)/2)
for i in range(0, c):
    sum_p += a[i]*0.7
max_t = a[c-1]
for i in range(c, len(a)):
    sum_p += a[i]


print(sum_p, max_t)
