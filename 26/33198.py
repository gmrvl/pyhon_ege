file = open('33198.txt')

a = []
first = file.readline().split(' ')
n = int(first[0])
s = int(first[1])
summ = 0
count = 0
for i in file:
    i = int(i)
    if 200 < i < 210:
        summ += i
        count += 1
    else:
        a.append(i)

a = sorted(a)

for i in a:
    if summ + i <= s:
        summ += i
        count += 1
    else:
        break

b = sorted(a, reverse=True)

for d in range(count -1, 0, -1):
    last = a[d]  # last - тот груз, который хотим заменить

    for i in range(d + 1, len(a)):
        if summ - last + a[i] <= s:
            summ = summ - last + a[i]
        else:
            break

print(summ, count)
