# Определите количество троек, в которых хотя бы один из трёх элементов меньше,
# чем среднее арифметическое всех чисел в файле,
# и десятичная запись хотя бы одного из трёх элементов оканчивается на 6.
# В ответе запишите два числа: сначала количество найденных троек,
# а затем – максимальную сумму элементов таких троек.

file = open('4675.txt')
count = 0
summ = 0
for i in file:
    i = int(i)
    summ += i
    count += 1

average = summ // count

file = open('4675.txt')
count = 0
lastlast = int(file.readline())
last = int(file.readline())
maxSum = 0
for i in file:
    i = int(i)
    if (lastlast % 10 == 6 or last % 10 == 6 or i % 10 == 6) and (
            (lastlast < average) or (last < average) or (i < average)):
        count += 1
        summ1 = lastlast + last + i
        if summ1 > maxSum:
            maxSum = summ1
    lastlast = last
    last = i
print(count, maxSum)

