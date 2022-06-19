# Определите количество пар, в которых хотя бы один из двух элементов делится на 3
# и хотя бы один из двух элементов меньше среднего арифметического всех чётных элементов последовательности.

file = open("40733.txt")

count = 0
summ = 0

for i in file:
    i = int(i)
    if i % 2 == 0:
        summ += i
        count += 1
average = summ//count
file = open("40733.txt")
count = 0
maxPair = 0
last = int(file.readline())
for i in file:
    i = int(i)
    if (i % 3 == 0 or last % 3 == 0) and (i < average or last < average):
        count += 1
        if last + i > maxPair:
            maxPair = last + i
    last = i
print(maxPair, count)


