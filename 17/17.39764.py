file = open('39764.txt')

last_last = int(file.readline())
last = int(file.readline())

max_sum = 0
count = 0

for i in file:
    current = int(i)
    a = [last, last_last, current]
    a = sorted(a)
    if a[2]*a[2] == a[0]*a[0] + a[1]*a[1]:
        count += 1
        if a[0]+a[1]+a[2] > max_sum:
            max_sum = a[0]+a[1]+a[2]
    last_last = last
    last = current

print(max_sum, count)
