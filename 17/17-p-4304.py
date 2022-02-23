file = open('17-p-4304.txt')

max_pair = -20000
count = 0
last = int(file.readline())

for d in file:
    d = int(d)
    if last % 2 == 0:
        if last % 4 == 0 and d % 2 == 1 and d % 11 == 0:
            count += 1
            if last + d > max_pair:
                max_pair = last + d
    else:
        if d % 4 == 0 and last % 11 == 0:
            count += 1
            if last + d > max_pair:
                max_pair = last + d
    last = d

print(count, max_pair)
