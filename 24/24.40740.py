file = open('40740.txt').read()

line = ''
maxCount = 0

for i in file:
    if i != 'A':
        line += i
    else:
        if line.count('E') >= 3:
            if len(line) > maxCount:
                maxCount = len(line)
        line = ''
print(maxCount)
