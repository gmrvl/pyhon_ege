file = open("24-179.txt").read()

a = []
a.append(0)
a.append(0)
a.append(0)
# a[0] == c
# a[1] == d
# a[2] == e

position = 0
count = 0
third = 3

for d in file:
    if d == 'C' and position == 0:
        position = 1
    elif d == 'C' and position == 4:
        count += 1
        position = 1
        a[third] += 1
    elif d == 'C' and position == 2:
        position = 3
        third = 0
    elif d == 'B' and position == 1:
        position = 2
    elif d == 'B' and position == 3:
        position = 4
    elif d == 'D' and position == 2:
        position = 3
        third = 1
    elif d == 'E' and position == 2:
        position = 3
        third = 2
    else:
        position = 0

print(a, count)