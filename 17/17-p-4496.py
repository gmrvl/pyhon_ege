file = open('17-p-4496.txt')

count = 0
max_pair = -20001

last = int(file.readline())

for i in file:
    i = int(i)
    if last % 2 == 0:
        if i % 2 == 0 and i % 37 == last % 37:
            count += 1
            if i + last > max_pair:
                max_pair = i + last
    else:
        if i % 2 == 1 and i % 37 == last % 37:
            count += 1
            if i + last > max_pair:
                max_pair = i + last
    last = i

print(count, max_pair)
