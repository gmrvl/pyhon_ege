file = open('27694.txt').read()

last = ''
count = 0
maxCount = 0

for i in file:
    if i == 'B' or i == 'C':
        if last == 'A':
            count += 1
        else:
            if count > maxCount:
                maxCount = count
            count = 0
    if i == 'A':
        if last == 'B' or 'C':
            count += 1
        else:
            if count > maxCount:
                maxCount = count
            count = 1
    last = i
print(maxCount)
