file = open('36879.txt')

d = []
maxR = 0
for line in file:
    if line.count('G') < 25:
        d.append(line)
alth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for line in d:
    for i in alth:
        if line.rfind(i) - line.find(i) > maxR:
            maxR = line.rfind(i) - line.find(i)
print(maxR)

