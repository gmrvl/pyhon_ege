# Определите символ, который чаще всего встречается в файле сразу после буквы A.

file = open('33196.txt').read()

a = []
lastA = False
for i in range(100):
    a.append(0)

for i in file:
    if lastA:
        a[ord(i)] += 1
    if i == 'A':
        lastA = True
    else:
        lastA = False
max_l = chr(a.index(max(a)))

print(max_l)

