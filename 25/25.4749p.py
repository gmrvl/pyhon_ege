# сумма трёх наибольших нетривиальных делителей числа N
# Если у числа N меньше трёх таких делителей, то S (N) считается равным 0
# Найдите 5 наименьших натуральных чисел
# S (N) все цифры расположены в порядке неубывания


import math

n = 10_000_000
count = 0

while True:
    a = []  # массив делителей
    s = 0
    stop = int(math.sqrt(n))
    for i in range(2, stop):
        if n % i == 0:
            res = n // i
            a.append(res)
        if len(a) == 3:
            break
    if len(a) == 3:
        s = a[0]+a[1]+a[2]
    s = str(s)
    # print(a, s, n)

    for i in range(0, len(s)-1):
        if s[i] <= s[i+1]:
            continue
        else:
            s = False
            break

    if s != False and s!='0':
        count += 1
        print(s)

    if count == 5:
        break

    n += 1
