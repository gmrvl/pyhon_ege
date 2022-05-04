file = open('27697.txt').read()

last = 0
count = 0
max_count = 0
for i in file:
    if i == 'D':
        count += 1
    else:
        if count > max_count:
            max_count = count
        count = 0
    if count > max_count:
        max_count = count
    last = i
print(max_count)
