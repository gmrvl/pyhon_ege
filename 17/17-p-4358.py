file = open('4358.txt')

count = 0
maxD = 0

for i in file:
    i = hex(int(i))[2:]

    if i[-1] == '9' and i[-2] != 'A':
        count += 1
        if int(i, 16) > maxD:
            maxD = int(i, 16)
print(count, maxD)
