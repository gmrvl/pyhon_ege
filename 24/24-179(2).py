import re
a = []
for i in range(3):
    a.append(0)
file = open("24-179.txt").readline()
result = re.findall(r'CB[^ABF]BC', file)
for d in result:
    if d[2] == 'C':
        a[0] += 1
    if d[2] == 'D':
        a[1] += 1
    if d[2] == 'E':
        a[2] += 1

print(len(result), a)

