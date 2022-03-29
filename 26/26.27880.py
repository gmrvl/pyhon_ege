file = open('27880.txt')

a = file.readline().split(' ')
s = int(a[0])
n = int(a[1])

p = []
for i in file:
    p.append(int(i))
p = sorted(p)

count = 0
sum = 0
max_d = 0
for i in p:
    if i + sum <= s:
        sum += i
        count += 1
        max_d = i

print(count)
sum = sum - max_d
for i in range(1, n):
    if sum + p[i] <= s:
        max_d = p[i]
    else:
        break
print(max_d)

