file = open('36037.txt').read()

count = 0  # количество символов в текущей строке
maxCount = 0  # максимальное количество символов
last = ''

for i in file:
    if i == 'Y':
        if last == 'XZZ':
            if count > maxCount:
                maxCount = count
            count = 2
        last = 'Y'
        count += 1
    if i == 'X':
        last = 'X'
        count += 1
    if i == 'Z':
        last += i
        count += 1

print(maxCount)
