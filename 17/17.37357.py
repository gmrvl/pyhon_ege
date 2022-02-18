file = open('17.37357.txt')
a = []
maximums = []
total_sum = 0
max0 = 0
max4 = 0
# сумма делится на 8, когда сумма остатков деления каждого из двух чисел на 8 делится на 8
for i in range(8):
    a.append(0)

for i in range(8):
    maximums.append(0)

for d in file:
    x = int(d)

    if x % 8 == 0:
        total_sum += a[0]
    if x % 8 == 4:
        total_sum += a[4]
    if x % 8 == 1:
        total_sum += a[7]
    if x % 8 == 2:
        total_sum += a[6]
    if x % 8 == 3:
        total_sum += a[5]
    if x % 8 == 5:
        total_sum += a[3]
    if x % 8 == 6:
        total_sum += a[2]
    if x % 8 == 7:
        total_sum += a[1]
    a[x % 8] += 1

    if x % 8 == 0:
        if maximums[0] < x:
            max0 = maximums[0]
            maximums[0] = x
        elif max0 < x:
            max0 = x
    elif x % 8 == 4:
        if maximums[4] < x:
            max4 = maximums[4]
            maximums[4] = x
        elif max4 < x:
            max4 = x
    else:
        if maximums[x % 8] < x:
            maximums[x % 8] = x

print(total_sum, max(maximums[1]+ maximums[7], maximums[2]+maximums[6], maximums[3]+maximums[5], maximums[0]+ max0, maximums[4]+max4))