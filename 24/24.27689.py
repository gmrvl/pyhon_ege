#  Определите максимальную длину цепочки вида XYZXYZXYZ... (составленной из фрагментов XYZ, последний фрагмент может быть неполным).

file = open("27689.txt").read()

count = 0
max_count = 0
last = None

for i in file:
    if i == "X":
        if last == "Z" or last == None:
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 1
    if i == "Y":
        if last == "X":
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    if i == "Z":
        if last == "Y":
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    last = i

if count > max_count:
    max_count = count
print(max_count)

