file = open('45258.txt').read()

count = 0
maxCount = 0
last = ''
for i in file:
    if i == 'A' or i == 'C':
        if last == 'B':
            count += 1
        else:
            count -= 1
            if count > maxCount:
                maxCount = count
            count = 1
    if i == 'B':
        if last == 'A' or last == 'C':
            count += 1
        else:
            if count > maxCount:
                maxCount = count
            count = 0
    last = i
print(maxCount / 2)
