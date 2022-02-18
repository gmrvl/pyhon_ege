import math

n = 452021
count = 0

while True:
    n += 1
    min_d = 0
    max_d = 0
    stop = int(math.sqrt(n))
    for i in range(2, stop):
        if n % i == 0:
            min_d = i
            max_d = n // i
            break
    if (max_d + min_d) % 7 == 3:
        print(n, max_d + min_d)
        count += 1
    if count == 5:
        break