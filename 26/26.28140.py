file = open('28140.txt')

a = []
s, n = file.readline().split(' ')
s = int(s)

for i in file:
    a.append(int(i))
a = sorted(a)

count = 0
summ = 0

for i in a:
    if summ + i <= s:
        summ += i
        count += 1
    else:
        break

max_d = a[count-1]
summ -= max_d

for i in range(count, int(n)):
    if summ + a[i] <= s:
        max_d = a[i]
    else:
        break
print(count, max_d)

