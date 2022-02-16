#  Определите максимальную длину цепочки вида ABABAB... (составленной из фрагментов AB, последний фрагмент может быть неполным)

file = open('27694.txt').read()

count = 0
max_count = 0
last = 0

for i in file:
    if i == 'A':
        if count == 0 or last == 'B':
            count += 1
        else:
            if max_count < count:
                max_count = count
            count = 1
    if i == 'B':
        if last == 'A':
            count += 1
        else:
            if max_count < count:
                max_count = count
            count = 0
    if i == 'C':
        if max_count < count:
            max_count = count
        count = 0
    last = i

if max_count < count:
    max_count = count

print(max_count)
