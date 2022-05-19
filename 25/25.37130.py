import math

n = 600000
count = 0
while True:
    n += 1
    stop = int(math.sqrt(n))
    a = []
    for i in range(2, stop):
        if n % i == 0:
            if i != 7 and i % 10 == 7:
                a.append(i)
            elif (n // i) % 10 == 7:
                a.append(n // i)
    if len(a) > 0:
        a = sorted(a)
        print(n, a[0])
        count += 1
    if count >= 5:
        break
