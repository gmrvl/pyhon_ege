import math

n = 600000
count = 0
while True:
    n += 1
    stop = int(math.sqrt(n))
    for i in range(2, stop):
        if n % i == 0:
            if i != 7 and i % 10 == 7:
                print(n, i)
                count += 1
    if count >= 5:
        break