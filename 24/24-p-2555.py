#  Определите количество строк, в которых буква S встречается столько же раз, сколько и буква X

file = open('24-p-2555.txt')

count = 0

for string in file:
    if string.count('S') == string.count('X'):
        count += 1

print(count)
