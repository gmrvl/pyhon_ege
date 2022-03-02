#  Определите количество строк, в которых буква E встречается чаще, чем буква A.
file = open('29672.txt')
count = 0
for i in file:
    if i.count('E') > i.count('A'):
        count += 1
print(count)