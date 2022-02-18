#  Определите символ, который чаще всего встречается в файле сразу после буквы E.

file = open('33494.txt').read()

a = []
for i in range(3000):
    a.append(0)

last_e = False
for i in file:
    if last_e:
        a[ord(i)] += 1
    if i == 'E':
        last_e = True
    else:
        last_e = False


print(chr(a.index(max(a))))
