file = open('36039.txt')

a = []
first = file.readline().split(' ')

s = int(first[0])
n = int(first[1])

for i in file:
    i = int(i)
    a.append(i)
a = sorted(a)

count = 0
sum_w = 0

for i in a:
    if sum_w + i <= s:
        sum_w += i
        count += 1
    else:
        break

sum_w -= a[count - 1]
max_w = a[count - 1]

for i in range(count, n):
    if sum_w + a[i] <= s:
        max_w = a[i]
    else:
        break
print(count, max_w)