file = open('27882.txt')

n = int(file.readline().split(' ')[0])
a = []
sum = 0

for i in file:
    a.append(int(i))

a = sorted(a)

for i in a:

    if sum + i < n:
        sum += i
    else:
        break

print(n, sum)
