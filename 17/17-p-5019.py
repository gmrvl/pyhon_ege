#  Определите сначала количество пар, в которых оба числа больше,
#  чем сумма всех цифр «7» в восьмеричной записи всех чисел в файле,
#  а затем минимальную из сумм таких пар
file = open('5019.txt')

count7 = 0
for i in file:
    i = oct(int(i))[2:]
    count7 += i.count('7')
count7 *= 7

file = open('5019.txt')

count = 0
minSum = 2001
last = int(file.readline())

for i in file:
    i = int(i)
    if i > count7 and last > count7:
        count += 1
        if last + i < minSum:
            minSum = last + i
    last = i
print(count, minSum)
