file = open("40992.txt")
a = []
count = 0
max_s = 0

for line in file:
    a.append(int(line))

count_nch = 0
sum_nch = 0
for digit in a:
    if digit % 2 == 1:
        count_nch += 1
        sum_nch += digit

average = sum_nch / count_nch

for i in range(0, len(a) - 1):
    if a[i] % 5 == 0 or a[i + 1] % 5 == 0:
        if a[i] < average or a[i + 1] < average:
            count += 1
            if a[i] + a[i + 1] > max_s:
                max_s = a[i] + a[i + 1]
print(count, max_s)
input("end")
