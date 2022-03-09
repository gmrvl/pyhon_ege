file = open('37159.txt').read()
count = 0
maks = 0
last = None
for d in file:
    if d == 'a':
        if last == 'd':
            if count > maks:
                maks = count
            count = 1
        else:
            count += 1
    elif d == 'd':
        if last == 'a':
            if count > maks:
                maks = count
            count = 1
        else:
            count += 1
    else:
        count += 1

    last = d
print(maks)
