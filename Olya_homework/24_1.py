file = open('24_1.txt')

max_count = 0

alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

a = []  # тут храним последний индекс)
for j in range(len(alp)):
    a.append(False)

for str in file:
    for i in a:
        a[i] = False
    if str.count('A') < 25:
        range = 0
        for i in str:
            if a[alp.find(i)] == False:
                a[alp.find(i)] = range
            elif range - a[alp.find(i)] > max_count:
                max_count = range - a[alp.find(i)]
            print(max_count)

            a[alp.find(i)] = range
            range += 1
print(max_count)
