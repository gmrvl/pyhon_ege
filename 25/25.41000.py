import math

n = 11000000
count = 0
while True:
    n += 1
    a = []
    stop = int(math.sqrt(n))
    for d in range(2, stop):
        if n % d == 0:
            a.append(d)
            a.append(n // d)
    a = sorted(a)
    m = 0
    if len(a) >= 2:
        m = a[-1] + a[-2]
    if 0 < m < 10000:
        print(n, m)
        count += 1
        if count >= 5:
            break
