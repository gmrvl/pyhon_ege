file = open('4142.txt').read()
count = 0
max_count = 0
last = None

for i in file:
    if i == 'X':
        if last == 'Z' or last == None:
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 1
    elif i == 'Y':
        if last == 'X' or last == None:
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 1
    elif i == 'Z':
        if last == 'Y' or last == None:
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 1
    else:
        if count > max_count:
            max_count = count
        count = 0
    last = i
print(max_count)

