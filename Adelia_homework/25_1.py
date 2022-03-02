import math

count = 0
for i in range(245690, 245757):
    count += 1
    pr = True
    stop = int(math.sqrt(i))
    for j in range(2, stop):
        if i % j == 0:
            pr = False
            break
    if pr == True:
        print(count, i)
