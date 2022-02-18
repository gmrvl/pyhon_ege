file = open("24.27699.txt").read()

last = ''
count = 0
max_count = 0

for d in file:
    if d == 'L':
        if last == '' or count == 0:
            count += 1
        elif count != 0 and last == 'R':
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 1

    elif d == 'D':
        if count != 0 and last == 'L':
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0

    elif d == 'R':
        if count != 0 and last == 'D':
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    last = d

print(count, max_count)