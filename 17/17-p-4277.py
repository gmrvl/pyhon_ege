file = open('17-1.txt')

count = 0
maxCount = 0
last = int(file.readline())
countP = 0

for i in file:
    i = int(i)

    if i < last:
        count += 1
    else:
        if count > maxCount:
            maxCount = count
            countP = 1
        elif count == maxCount:
            countP += 1
        count = 1
    last = i
if count > maxCount:
    maxCount = count
print(countP, maxCount)
