file = open('17dosrok.txt')

a = []
count = 0
maxSum = 0

for i in file:
    i = int(i)
    if i % 17 == 0:
        a.append(i)

a = min(a)
# file.close()
file = open('17dosrok.txt')
last = int(file.readline())
for i in file:
    i = int(i)
    if i % a == 0 or last % a == 0:
        count += 1
        if i + last > maxSum:
            maxSum = i + last
    last = i
print(count, maxSum)
